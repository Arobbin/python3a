"""
Assignment 1: Print Header by Arob

Assignment 2: temperature conversion
"""
# Assignment 1
def print_header():
    print("STEM Center Temperature Project")
    print("Alex Robinson")

# Assignment 2
# def convert_units(celsius_value, units):
#     if units == 0:
#         val = celsius_value
#     elif units == 1:
#         val = (celsius_value * 9/5 + 32)
#     elif units == 2:
#         val = (celsius_value + 273.15)
#     else:
#         print('please enter value of 1, 2, or 3')
#     return val

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





def main():
    print_header()
    # celsius_value = float(input("please enter temp: "))
    # units = int(input("please enter units either 1, 2, or 3: "))
    # convert_units(celsius_value, units)
    answer = 10
    while answer > 8:
        try:
            print_menu()
            answer = int(input("Select number between 1 and 7: "))
            if answer == 1:
                new_file(None)
            elif answer == 2:
                choose_units(None)
            elif answer == 3:
                change_filter(None, None)
            elif answer == 4:
                print_summary_statistics(None)
            elif answer == 5:
                print_temp_by_day_time(None, None)
            elif answer == 6:
                print_histogram(None, None)
            elif answer == 7:
                print("exiting application")
                break     
        except:
            print('you entered an incorrect entry, try again.')
            
             

        
       
            


if __name__ == "__main__":
    main()