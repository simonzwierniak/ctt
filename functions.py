from user_inputs import *

# Function for currency converter
# Requires live data from internet?
def currency_converter():
    pass

class Temperature:
    def __init__(self, temp, unit):
        self.temp = temp
        self.unit = unit

    def temp_converter(temp, unit):
        temp = float(temp)
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
    def __init__(self, weight, unit):
        self.unit = unit
        self.weight = weight

    def weigth_converter(weight, unit):
        weight = float(weight)
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
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def distance_converter(value, unit):
        if unit.lower() == 'km':
            result = round((float(value) * 0.621371), 2)
            return (f"{value} km = {result} miles.")   

        if unit.lower() == 'miles':
            result = round((float(value) * 1.609344), 2)
            return (f"{value} miles = {result} km.")
        
        else:
            print("Error: wrong input")
            return None
    
    def length_converter(length, unit):
        length = float(length)
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
