from functions import Distance, Weight, Temperature, Currency
from user_inputs import *
import argparse

def main():
    currency_pairs = Currency.get_available_currencies()
    available_currency_codes = []
    if currency_pairs:
        available_currency_codes = [pair[0] for pair in currency_pairs]

    parser = argparse.ArgumentParser(description="Convertisseur Tout Terrain to help me convert stuff while writing articles.")
    parser.add_argument('-v', action='store', dest='user_value', help="Value to convert")
    parser.add_argument('-u', action='store', dest='user_unit', help="Unit to convert. Combo available: km/miles; cm/inch; kg/pds; C/F")
    parser.add_argument('-to', action='store', dest='user_unit_destination', help="Destination unit for currency conversion. Combo available: USD/EUR")
    parser.add_argument('-c', action='store_true', dest='user_get_currencies', help="List the currencies available")
    
    args = parser.parse_args()
    
    if args.user_get_currencies:
        return Currency.get_available_currencies()

    if args.user_value and args.user_unit:  # If command line arguments are provided
        user_value = args.user_value
        user_unit = args.user_unit
        
        if args.user_unit in ('km', 'miles'):
            return Distance.distance_converter(user_value, user_unit)

        elif args.user_unit in ('cm', 'inch'):
            return Distance.length_converter(user_value, user_unit)
        
        elif args.user_unit in ('kg', 'pds'):
            return Weight.weight_converter(user_value, user_unit)
        
        elif args.user_unit in ('C', 'F'):
            return Temperature.temp_converter(user_value, user_unit)
        
        elif (user_unit.upper() in available_currency_codes and 
              args.user_unit_destination and 
              args.user_unit_destination.upper() in available_currency_codes):
            return Currency.currency_converter(user_value, user_unit, args.user_unit_destination)
        
        else:
            print(f"Error: Invalid unit '{args.user_unit}'")
            return None
    
    if args.user_value or args.user_unit or args.user_unit_destination:
        parser.print_help()
        return None

    user_choice = get_welcome_input() # If no command line arguments, proceed with interactive input

    if user_choice == "1":
        value, unit = get_value_and_unit()
        return Distance.distance_converter(value, unit)
    
    elif user_choice == '2':
        length, unit = get_length_and_unit()
        return Distance.length_converter(length, unit)

    elif user_choice == "3":
        weight, unit = get_weight_and_unit()
        return Weight.weight_converter(weight, unit)
    
    elif user_choice == "4":
        temp, unit = get_temp_and_unit()
        return Temperature.temp_converter(temp, unit)
    
    elif user_choice == "5":
        value, unit_origin, unit_destination = get_currency_and_unit()
        return Currency.currency_converter(value, unit_origin, unit_destination)

    else:
        print("Error: wrong input")
        return None
        
if __name__ == "__main__":
    result = main()
    if result is not None:
        print(f"\n{result}")