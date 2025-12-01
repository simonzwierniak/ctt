def get_welcome_input():
    print("Welcome to the Convertisseur Tout Terrain (CTT).")
    return input("CTT available: km/miles (1), cm/inches (2), kg/pounds (3), temperature C/F (4), currency (5): ")

def get_value_and_unit():
    value = input("Value to convert: ")
    unit = input("Enter the unit (km, miles): ")
    return value, unit

def get_length_and_unit():
    value = input("Length to convert: ")
    unit = input("Enter the unit (cm, inch): ")
    return value, unit

def get_weight_and_unit():
    value = input("Enter the weight: ")
    unit = input("Enter the unit (kg, pds): ")
    return value, unit

def get_temp_and_unit():
    value = input("Enter the temperature: ")
    unit = input("Enter the unit (C, F): ")
    return value, unit

def get_currency_and_unit():
    value = input("Enter the amount to convert: ")
    unit_origin = input("Enter the origin currency (ex: USD, EUR): ")
    unit_destination = input("Enter the destination currency (ex: USD, EUR): ")
    return value, unit_origin, unit_destination