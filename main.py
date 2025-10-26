from functions import Distance, Weight
from user_inputs import *

def main():
    user_choice = get_welcome_input()

    if user_choice == "1":
        value = get_value()
        return Distance.kilometer_to_miles(value)
        
    elif user_choice == "2":
        value = get_value()
        return Distance.miles_to_kilometer(value)
    
    elif user_choice == "3":
        weight, unit = get_length_and_unit()
        return Weight.weigth_converter(weight, unit)
    
    else:
        print("Error: wrong input")
        return None
        
if __name__ == "__main__":
    result = main()
    if result is not None:
        print(f"\nConversion result: {result}")
