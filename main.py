from functions import Distance, Weight, Temperature
from user_inputs import *
import argparse

def main():
    parser = argparse.ArgumentParser(description="Convertisseur Tout Terrain to help me convert stuff while writing articles.")
    parser.add_argument('-v', action='store', dest='user_value', help="Value to convert")
    parser.add_argument('-u', action='store', dest='user_unit', help="Unit to convert. Combo available: km/miles; cm/inch; kg/pds; C/F")
    args = parser.parse_args()
    
    if args.user_value and args.user_unit:  # If command line arguments are provided
        if args.user_unit in ('km', 'miles'):
            value = args.user_value
            unit = args.user_unit
            return Distance.distance_converter(value, unit)

        elif args.user_unit in ('cm', 'inch'):
            length = args.user_value
            unit = args.user_unit
            return Distance.length_converter(length, unit)
        
        elif args.user_unit in ('kg', 'pds'):
            weight = args.user_value
            unit = args.user_unit
            return Weight.weight_converter(weight, unit)
        
        elif args.user_unit in ('C', 'F'):
            temp = args.user_value
            unit = args.user_unit
            return Temperature.temp_converter(temp, unit)
        else:
            print(f"Error: Invalid unit '{args.user_unit}'")
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

    else:
        print("Error: wrong input")
        return None
        
if __name__ == "__main__":
    result = main()
    if result is not None:
        print(f"\nConversion result: {result}")