""" Assignment Two: Temperature Conversions
    Submitted by Alex Robinson
    Submitted:  October 5, 2021

    Assignment 2: Add code to prompt the user for a temperature in Celsius and
    then converts that temperature to a specified different temperature
    unit.
    Assignment One: Opening Lines - Alex Robinson
 """

def print_greeting():
    print("STEM Center Temperature Project")
    print("Alex Robinson")

print(print_greeting())

celsius_value = float(input("please enter temp: "))
units = int(input("please enter units: "))

def convert_units():
    if units == 0:
        print(f'The Celsius temperature is {celsius_value}')
    elif units == 1:
        F = (celsius_value * 9/5 + 32)
        print(f'The Fahrenheit temperature is {F}')
    elif units == 2:
        K = (celsius_value + 273.15)
        print(f'The Kelvin temperature is {K}')
    else:
        print('invalid value for units. Please use 0, 1, or 2')
      
convert_units()