class Converter:
    def __init__(self, value):
        self.value = float(value)
    
    def celsius_to_fahrenheit(self):
        return (self.value * 9/5) + 32
    
    def fahrenheit_to_celsius(self):
        return (self.value - 32) * 5/9
    
    def kilometers_to_miles(self):
        return self.value * 0.621371
    
    def miles_to_kilometers(self):
        return self.value * 1.60934
    
    def kilograms_to_pounds(self):
        return self.value * 2.20462
    
    def pounds_to_kilograms(self):
        return self.value * 0.453592


    