import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_key") 
api_domain = "https://v6.exchangerate-api.com/v6" 

class Currency:

    @staticmethod
    def get_available_currencies():
        if not api_key:
            print("Error: API key not found. Please set your API key in the environment variables.")
            return None 
        url = f"{api_domain}/{api_key}/codes"
        try:
            response = requests.get(url, timeout=5) # GET request with 5 seconds timeout
            response.raise_for_status() # Raise an excep for bad status codes
            data = response.json() # Parse JSON response
            if 'supported_codes' in data:
                return data['supported_codes']
            else:
                print("Data error: 'supported_codes' not found in API.")
                return None
            
        except requests.exceptions.RequestException as e:
            print(f"API Error: {e}")
            return None
        
    @staticmethod
    def format_currencies_for_display():
        currency_list = Currency.get_available_currencies()
        if not currency_list:
            return "Failed to retrieve a currency list."
        formatted_list = ""
        for code, name in currency_list:
            formatted_list += f"{code}: {name}\n"
        return formatted_list.strip()

    @staticmethod
    def get_rate(base_currency, target_currency):
        base_currency = base_currency.upper()
        target_currency = target_currency.upper()
        if not api_key:
            print("Error: API key not found. Please set your API key in the environment variables.")
            return None
        url = f"{api_domain}/{api_key}/latest/{base_currency}"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            if 'conversion_rates' in data and target_currency in data['conversion_rates']:
                rate = data['conversion_rates'][target_currency]
                return rate
            else:
                print("Error: Invalid currency code or data not found.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"API Error: {e}")
            return None
        except KeyError:
            print("Data Error: Unexpected response structure from API.")
            return None
        
    @staticmethod
    def currency_converter(amount, base_currency, target_currency):
        try:
            amount = float(amount)
        except ValueError:
            print("Error: Invalid amount. Please enter a numeric value.")
            return None
        rate = Currency.get_rate(base_currency, target_currency)
        if rate is not None:
            converted_amount = round(amount * rate, 2)
            return (f"{amount} {base_currency.upper()} = {converted_amount} {target_currency.upper()}.")
        else:
            return None
        
class Temperature:
    @staticmethod
    def temp_converter(temp, unit):
        try:
            temp = float(temp)
        except ValueError:
            return "Invalid temperature value."
        
        if unit.lower() == 'c':
            result = round(((9/5 * temp) + 32), 2)
            return (f"{temp}°C = {result}°F.")
        
        if unit.lower() == 'f':
            result = round((5/9 * (temp - 32)), 2)
            return (f"{temp}°F = {result}°C.")
        
        else:
            print("Error: wrong input")
            return None
        
class Weight:
    @staticmethod
    def weight_converter(weight, unit):
        try:
            weight = float(weight)
        except ValueError:
            return "Invalid weight value."
        
        if unit.lower() == 'kg':
            result = round((weight * 2.204623), 2) # arrondi à deux chiffres après la virgule
            return (f"{weight} kg = {result} pds.")

        if unit.lower() == 'pds':
            result = round((weight * 0.4535924), 2)
            return (f"{weight} pds = {result} kg.")
        
        else:
            print("Error: wrong input")
            return None
            
class Distance:
    @staticmethod
    def distance_converter(value, unit):
        try:
            value = float(value)
        except ValueError:
            return "Invalid distance value."
        
        if unit.lower() == 'km':
            result = round((float(value) * 0.621371), 2)
            return (f"{value} km = {result} miles.")   

        if unit.lower() == 'miles':
            result = round((float(value) * 1.609344), 2)
            return (f"{value} miles = {result} km.")
        
        else:
            print("Error: wrong input")
            return None
    
    @staticmethod
    def length_converter(length, unit):
        try:
            length = float(length)
        except ValueError:
            return "Invalid length value."
        if unit.lower() == 'cm':
            result = round((length / 2.54), 2)
            return (f"{length} cm = {result} inches.")
        
        if unit.lower() == 'inch':
            result = round((length * 2.54), 2)
            return (f"{length} inches = {result} cm.")
            
        else:
            print("Error: wrong input")
            return None

# Habillage UI
def UI():
    pass
