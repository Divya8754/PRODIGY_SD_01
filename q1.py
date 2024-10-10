
def celsius_to_fahrenheit_kelvin(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

def fahrenheit_to_celsius_kelvin(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    return celsius, kelvin

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return celsius, fahrenheit

def temperature_converter():
    print("Temperature Conversion Program")
    
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of the temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

    if unit == 'C':
        fahrenheit, kelvin = celsius_to_fahrenheit_kelvin(temp)
        print(f"{temp}°C is {fahrenheit:.2f}°F and {kelvin:.2f}K")
    elif unit == 'F':
        celsius, kelvin = fahrenheit_to_celsius_kelvin(temp)
        print(f"{temp}°F is {celsius:.2f}°C and {kelvin:.2f}K")
    elif unit == 'K':
        celsius, fahrenheit = kelvin_to_celsius_fahrenheit(temp)
        print(f"{temp}K is {celsius:.2f}°C and {fahrenheit:.2f}°F")
    else:
        print("Invalid unit entered. Please enter C, F, or K.")

temperature_converter()