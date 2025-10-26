from user_inputs import *

# Function for currency converter
# Requires live data from internet
def currency_converter():
    pass

# Function for size converter
def size_converter():
    pass

# Function for weigth converter
class Weight:
    def __init__(self, weight, unit):
        self.unit = unit
        self.weight = weight

    def weigth_converter(weight, unit):
        weight = float(weight)
        if unit.lower() == 'kg':
            result = weight * 2.204623
            return (f"{weight} kg is {result} pds.")
        
        if unit.lower() == 'pds':
            result = weight * 0.4535924
            return (f"{weight} pds is {result} kg.")
        
        return None
            
# Converter for distances
class Distance:
    def __init__(self, value):
        self.value = value

    def kilometer_to_miles(value):
        result = float(value) * 0.621371
        return (f"{value} km is {result} miles.")
    
    def miles_to_kilometer(value):
        result = float(value) * 1.609344
        return (f"{value} miles is {result} km.")

# Habillage UI
def UI():
    pass
