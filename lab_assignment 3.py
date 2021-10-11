""" Assignment Two: Temperature Conversions
    Submitted by Alex Robinson
    Submitted:  October 5, 2021

    Assignment 2: Add code to prompt the user for a temperature in Celsius and
    then converts that temperature to a specified different temperature
    unit.
    
    Assignment 3: Write a function named print_menu()
 """

# Assignment 2


def convert_units(celsius_value, units):
    if units == 0:
        val = celsius_value
    elif units == 1:
        val = (celsius_value * 9/5 + 32)
    elif units == 2:
        val = (celsius_value + 273.15)
    else:
        print('please enter value of 1, 2, or 3')
    return val

# Assignment 3
def print_menu():
    print("""Main Menu---------
    1 - Process a new data file
    2 - Choose units
    3 - Edit room filter
    4 - Show summary statistics
    5 - Show temperature by date and time
    6 - Show histogram of temperatures
    7 - Quit""")
    
    def new_file(dataset):
        """
        Open a new file
        """
    print("New File Function Called")

    def choose_units():
        """
        Choose Units
        """
    print("Choosing Units")

    def change_filter(sensor_list, active_sensors):
        """
        Change Sensors and Filters
        """
    print("Changing Sensors and Filters")

    def print_sumnmary_statistics(dataset, active_sensors):
        """
        Printing Stats
        """
    print("Printing Stats")

    def print_temp_by_day_time(dataset, active_sensors):
        """
        Printing Temp by day and time
        """
    print("Printing Temp by day and time")

    def print_histogram(dataset, active_sensors):
        """
        Printing histogram
        """
    print("Printing histogram")
