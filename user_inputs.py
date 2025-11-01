def get_welcome_input():
    print("Welcome to the Convertisseur Tout Terrain (CTT).")
    return input("CTT available: km/miles (1), cm/inches (2), kg/pounds (3); temperature (4): ")

def get_value_and_unit():
    value = input("Value to convert: ")
    unit = input("Enter the unit (km, miles): ")
    return value, unit

def get_length_and_unit():
    length = input("Length to convert: ")
    unit = input("Enter the unit (cm, inch): ")
    return length, unit

def get_weight_and_unit():
    weight = input("Enter the weight: ")
    unit = input("Enter the unit (kg, pds): ")
    return weight, unit

def get_temp_and_unit():
    temp = input("Enter the temperature: ")
    unit = input("Enter the unit (C, F): ")
    return temp, unit