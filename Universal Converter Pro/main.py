"""
Multi-Purpose Converter Program
Author: Farzad Darwazi
Date: 2026-03-26

Description:
This Python program allows the user to convert between multiple types of units,
including:
- Currency (USD, EUR, JPY, GBP, etc)
- Temperature (Celsius, Fahrenheit, Kelven)
- Length (milimeters, centimeters, meters, kilometers, miles)
- Weight (kilograms, grams, pounds)

The user can select the type of conversion, enter a value, and specify source
and target units. The program then calculates and displays the converted value.

This program is designed to be easily extendable to add more conversion types
and units in the future.
"""

import sys
import os
from decimal import Decimal, InvalidOperation
import converters as cvt

def wipeScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main program starts here-------------------------------------------------------------------
def main():

    # Set UTF-8 encoding for Windows console
    if os.name == 'nt':
        os.system('chcp 65001 > nul')

    # main loop to keep the program running until the user decides to exit
    while True:

        # try-except block to handle unexpected errors and allow graceful exit
        try:
            print("Welcome to Farzad's Converter Program!")

            # loop to display the main menu and handle user input for conversion type
            while True:  
                
                cvt.main_menu()     #display main menu
            
                # try-except block to handle invalid input for conversion type selection
                try:
                    user_choice = int(input("Please select the type of conversion (1-4): "))
                    wipeScreen()    #clear the screen after user input

                    # check if the user wants to exit the program
                except ValueError:
                    wipeScreen()
                    print("Invalid input. Please enter a number between 1 and 4.")
                    continue

                # check if the user wants to exit the program (0)
                # or if the input is out of range (not between 1 and 4)
                if(user_choice == 0):
                    wipeScreen()
                    print("\nExiting the program. Goodbye!")
                    return 0    
                if(user_choice < 1 or user_choice > 4):
                    print("Invalid choice. Please select a number between 1 and 4.")
                    continue

                # match statement to call the appropriate function based on user choice
                match user_choice:

                    # each case corresponds to currency conversion
                    case 1:

                        # nested loop to display the currency conversion menu
                        # and handle user input for currency selection
                        while True:
                            cvt.currency_menu()     #display currency conversion menu
                            try:
                                pick_currency = int(input("Select a currency for conversion (0-20): "))
                                wipeScreen()

                                # check if the user wants to return to the main menu (0)
                                # or if the input is out of range (not between 0 and 20) 
                                if (pick_currency == 0):
                                    wipeScreen()
                                    print("Returning to the main menu.")
                                    break
                                if (pick_currency < 1 or pick_currency > 20):
                                    wipeScreen()
                                    print("Invalid choice. Please select a number between 0 and 20.")
                                    continue
                            except ValueError:
                                wipeScreen()
                                print("Invalid input. Please enter a valid number.")
                                continue

                            while True:
                                try:
                                    
                                    usdAmt = Decimal(input("Enter the amount of USD: "))
                                    wipeScreen()

                                    if (usdAmt < 0):
                                        wipeScreen()
                                        print("Invalid input. Please enter a positive number.")
                                        continue
                                    if (usdAmt == 0):
                                        wipeScreen()
                                        print("Returning to the currency conversion menu.")
                                        break;

                                except InvalidOperation:
                                    wipeScreen()
                                    print("Invalid input. Please enter a valid number.")
                                    continue

                                cvt.currency(pick_currency, usdAmt) 
                    
                    # each case corresponds to temperature conversion
                    case 2:
                       while True:    #while should be first--------------------
                           cvt.temp_menu()   
                           try:
                              
                                # to pick the type of temperature conversion (1-6) and handle invalid input
                                pick_temp = int(input("\nChoose your temperature conversion (1-6): "))
                                wipeScreen()

                                # check if the user wants to return to the main menu (0) 
                                # or if the input is out of range (not between 1 and 6)
                                if (pick_temp == 0):
                                    print("\nReturning to the main menu.\n")
                                    break
                                if (pick_temp < 1 or pick_temp > 6):
                                    print("\nInvalid choice. Please select a number between 1 and 6.\n")
                                    continue
                           except ValueError:
                                    wipeScreen()
                                    print("\nInvalid input. Please enter a valid number.\n")
                                    continue

                           while True:
                                
                               # First take vakue in string format
                                tempStr = input("\nEnter the temperature: ").strip()
                                wipeScreen()
                                    
                                if tempStr == 'q':
                                    wipeScreen()
                                    print("\nReturning to the temperature conversion menu.\n")
                                    break
                                
                                try:

                                    # Now try to convert the string input to a float
                                    temp = Decimal(tempStr)
                                    wipeScreen()
                                    
                                except InvalidOperation:
                                    wipeScreen()
                                    print("\nInvalid input. Please enter a valid number.\n")
                                    continue
                                cvt.temperature(pick_temp, temp)

                    # each case corresponds to length conversion
                    case 3:

                        # nested loop to display the length conversion menu
                        # and handle user input for length conversion selection
                        wipeScreen()

                        # the length conversion is a bit more complex because
                        # it requires two unit selections (initial and final)
                        while True:
                            try:

                                # display the initial unit selection menu and handle
                                # user input for the initial unit selection (1-4)
                                # and wipe the screen after input
                                cvt.length_initial_menu()
                                len1 = int(input('Enter chosen measurement (1-4): '))
                                wipeScreen()

                                # check if the user wants to return to the main menu (0)
                                # or if the input is out of range (not between 1 and 4)
                                if (len1 == 0):
                                    print('Returning to the main menu.')
                                    wipeScreen()
                                    break
                                if (len1 < 1 or len1 > 4):
                                    wipeScreen()
                                    print('Invalid input. Try again (1-4)')
                                    continue

                            except ValueError:
                                wipeScreen()
                                print('Invalid input. Try again (1-4)')
                                continue    
                            
                            # nested loop to display the final unit selection menu
                            # and handle user input for the final unit selection (1-4)
                            # and wipe the screen after input
                            while True:
                                try:

                                    # display the final unit selection menu and handle
                                    # user input for the final unit selection (1-4) 
                                    # and wipe the screen after input
                                    cvt.length_final_menu()
                
                                    len2 = int(input('Enter chosen measurement (1-4): '))
                                    wipeScreen()
                                    if (len2 == 0):
                                        wipeScreen()
                                        print('Returning to the (initial) unit.')
                                        break
                                    if (len2 < 1 or len2 > 4):
                                        wipeScreen()
                                        print('Invalid input. Try again (1-4)')
                                        continue
                                    wipeScreen()
                                    break                        
                                except ValueError:
                                    wipeScreen()
                                    print('Invalid input. Try again (1-4)')
                
                            # nested loop to handle user input for the measurement value 
                            # to convert and call the length conversion function with 
                            # the selected initial unit, final unit, and measurement 
                            # value. This loop also handles invalid input for the 
                            # measurement value and allows the user to return to the 
                            # previous menu if they wish.
                            while True:
                                try:
                                    if(len2 == 0):
                                        wipeScreen()
                                        print('Returning to the (initial) unit.')
                                        break

                                    # ask for the measurement value to convert and wipe
                                    # the screen after input
                                    dist = Decimal(input('Input measurement value: '))
                                    wipeScreen()

                                    if(dist == 0):
                                        wipeScreen()
                                        print('Returning')
                                        break
                                    if(dist < 0):
                                        wipeScreen()
                                        print('Invalid input. Please enter a positive number.')
                                        continue

                                except InvalidOperation:
                                    wipeScreen()
                                    print('Invalid input. Please enter a valid number.')
                                    continue

                                # call the length conversion function with the selected 
                                # initial unit, final unit, and measurement value
                                cvt.length(len1,len2,dist)
                    case 4:
                        while True:
                            cvt.weight_initial_menu()
                            try:
                                wgt1 = int(input("Select a weight for conversion (0-11): "))
                                wipeScreen()
                                if (wgt1 == 0):
                                    wipeScreen()
                                    print("Returning to the main menu.")
                                    break
                                if (wgt1 < 1 or wgt1 > 11):
                                    wipeScreen()
                                    print("Invalid choice. Please select a number between 0 and 11.")
                                    continue
                            except ValueError:
                                wipeScreen()
                                print("Invalid input. Please enter a valid number.")
                                continue
                            cvt.weight_final_menu()
                            try:
                                wgt2 = int(input("Select a weight for conversion (0-11): "))
                                wipeScreen()
                                if (wgt2 == 0):
                                    wipeScreen()
                                    print("Returning to the main menu.")
                                    break
                                if (wgt2 < 1 or wgt2 > 11):
                                    wipeScreen()
                                    print("Invalid choice. Please select a number between 0 and 11.")
                                    continue
                            except ValueError:
                                wipeScreen()
                                print("Invalid input. Please enter a valid number.")
                                continue

                            while True:
                                try:
                                    weight = Decimal(input("Enter the weight: "))
                                    wipeScreen()
                                    if (weight < 0):
                                        wipeScreen()
                                        print("Invalid input. Please enter a positive number.")
                                        continue
                                    if (weight == 0):
                                        wipeScreen()
                                        print("Returning to the weight conversion menu.")
                                        break;
                                except InvalidOperation:
                                    wipeScreen()
                                    print("Invalid input. Please enter a valid number.")
                                    continue
                                cvt.weight(wgt1, wgt2 , weight)  
        
        # except block to catch any unexpected errors and print an error message
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting gracefully.")
            return 0

        # except block to catch EOFError (end of input) and print a message before exiting
        except EOFError:
            print("\nEnd of input detected. Exiting gracefully.")
            return 0

if __name__ == "__main__":
    main()                   


                

                



 
    
    
        

    


    

            

