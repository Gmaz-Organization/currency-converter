#importing needed modules
import find_currency as fc
from unit_testing import GenericError, InputError, WrongInputError
from currencies_data import all_currencies_dict as asd
import subprocess
from time import sleep
import sys
import os


#function for finding temporary directory of added files
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#finding temporary directory of added files
path_1 = resource_path(r'sysConfig\runtimeSett.bat')
path_2 = resource_path(r'sysConfig\exit.bat')


#taking data from currency data file and creating a list of currencies
asd_short = [n for n in asd.keys()]
asd_full_name = [n for n in asd.values()]

#running a batch file to set the runtime settings
subprocess.call([r'{}'.format(path_1)])

#home screen printing
print("WELCOME TO THE CURRENCY CONVERTER by Gmaz!\n")

msg = ""
print("All available currencies:")
for n in asd_short:
  msg += n + " "
  if len(msg) >= 60: #to make the output more readable and pretty
    print(msg)
    msg=""
print("\nExample input: 23 HRK USD\n")

#main app loop
while True:
  #asking for input from user
  value_list = input("Enter value, its currency and currency to covert to, \
put a space in between:\n").split() #input: 75 HRK EUR

  try:
    #checking if the list got 3 values
    if len(value_list) != 3:
      raise InputError

    else:
      #checking other input errors
      if (value_list[1].upper() not in asd_short) or (value_list[2].upper() not in asd_short):
        raise WrongInputError

      try:
        #asking for the amount of days to check the history of conversion and checking for errors in input
        value_list[0] = float(value_list[0])
        days_input = input("To work with a conversion rate of x days ago add x example: '4', otherwise '0 or 1': ")

        #checking if the input is a number and making sure its not None type
        if isinstance(days_input, str) and days_input.isdigit() and days_input != None:
          history_conv = int(days_input) - 1

        else:
          history_conv = 0

      #raising custom error if test fails
      except:
        print("Amount not correctlly specified!")
        raise GenericError

      #making sure that the arguments of the get_rates function are valid
      if not history_conv or history_conv < 0: 
        history_conv = 0

      #preparing function arguments
      value_list[1] = value_list[1].upper()
      value_list[2] = value_list[2].upper()

      #functiom from find_currency 
      value_converted, time = fc.get_rates(value_list[0], value_list[1], value_list[2], history_conv)
      
      #output
      print(f"{value_list[0]} of {asd[value_list[1]]} converted to {asd[value_list[2]]} is {str(value_converted)} {value_list[2]} at date: {str(time)}")
      print("")

      #checking if user wants graphical representation
      if (history_conv != 0):
        runGraph = input("Do you want to see a visual representation of conversion rate: Y/N? ")

        #drawing the graph
        if runGraph in ("y", "Y"):
          fc.draw_graph(value_list[0], value_list[1], value_list[2])


  #different errors testing
  except GenericError as error:
    print("Check your input, error was raised!")
    
  except InputError as error:
    print("Error while inputing data, check your input!")
    print("You must use space¨between inputs and add all three arguments!")

  except WrongInputError as error:
    print("Choice of currency does not exist in our data!")

  #asking if user wants to run again or exit
  finally:
    #checking repeat
    convert_again = input("Press any key to go again, or just enter to exit: ")
    if not(convert_again): break
    print("\n-------------------------------------------------\n")


#exiting the program
print("Exiting the program...",)
for n in range(3):
  print(".")
  sleep(0.4)

sleep(0.6)
subprocess.call([r'{}'.format(path_2)])