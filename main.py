from functions import Distance, Weight, Temperature
from user_inputs import *

def main():
    user_choice = get_welcome_input()

    if user_choice == "1":
        value, unit = get_value_and_unit()
        return Distance.distance_converter(value, unit)
    
    elif user_choice == '2':
        length, unit = get_length_and_unit()
        return Distance.length_converter(length, unit)

    elif user_choice == "3":
        weight, unit = get_weight_and_unit()
        return Weight.weigth_converter(weight, unit)
    
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