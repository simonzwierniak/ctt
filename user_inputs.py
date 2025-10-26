def get_welcome_input():
    print("Welcome to the Convertisseur Tout Terrain (CTT).")
    return input("CTT available: km to miles (1), miles to km (2), weigth converter (3): ")

def get_value():
    return input("Value to convert: ")

def get_length_and_unit():
    weight = float(input("Enter the weight: "))
    unit = input("Enter the unit (kg, pds): ")
    return weight, unit