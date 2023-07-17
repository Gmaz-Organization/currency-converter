#importing needed modules
import customtkinter
from tkinter import *
import find_currency as fc
from currencies_data import all_currencies_dict as asd
import os
import sys

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
path_apperaance = resource_path(r"apperanceConfig\gmaz_theme_v2.json")
path_icon = resource_path(r"apperanceConfig\converter_white_dark.ico")
#customize
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(r"{}".format(path_apperaance))
root = customtkinter.CTk()
root.title("Currency Converter")
root.iconbitmap(r"{}".format(path_icon))

#window set and it can't be moved
root.geometry("500x500")
root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)

#sort imported data
asd_short = [n for n in asd.keys()]
asd_full_name = [n for n in asd.values()]

#global variables
s_currency_1 = "" #short currency names, per example EUR for Euro 
s_currency_2 = ""
history_conv = 0 #using conversion rate from history_conv days ago

#click convert button
def convert():
  global value 
  try:
    value = float(e1.get()) #stirng frome entry box 1 to number 
    days_input = e2.get() #form entry box 2

    #checking if the input form entry box 2 is valid
    if isinstance(days_input, str) and days_input.isdigit() and days_input != None:
          history_conv = int(days_input) - 1 #form string to number
    else:
      history_conv = 0

    #graph works for dates in the last year(365 days)
    if (history_conv<=365 and history_conv>=0):
      global currency_1
      global currency_2
      currency_1 = optionmenu_1.get() #selected currency from option menu 1
      currency_2 = optionmenu_2.get() #selected currency from option menu 2
      global s_currency_1
      global s_currency_2
    
      #functiom from find_currency
      #finding shorts for selected currencys
      for i, cur in enumerate(asd_full_name, 0):
        if currency_1 == cur: s_currency_1 = asd_short[i]
        if currency_2 == cur: s_currency_2 = asd_short[i]

      #functiom from find_currency
      #findin the conversion value
      #date is stored in variable time
      value_converted, time = fc.get_rates(value, s_currency_1, s_currency_2, history_conv)

      #output if we had a successful conversion
      output_text=(f"{str(round(value,2))} of {currency_1} equals {round(value_converted,2)} {currency_2}\n\
    Currency rate: 1 {s_currency_1} = {round(value_converted/value, 5)} {s_currency_2} at date: {str(time)}")
      global output
      output.destroy()
      output = customtkinter.CTkLabel(master=output_frame, text=output_text)
      output.grid(row=0, column=0, pady=10, padx=10)

      #enable graph button if user enters at least yesterdays conversion rate
      if (history_conv>=1): 
        graph_button.configure(state="enabled")

    else:
      output.destroy()
      output = customtkinter.CTkLabel(master=output_frame, text="Sorry. You can search only up to 365 days ago.\nTry again.")
      output.grid(row=0, column=0, pady=10, padx=10)

  except: 
    #for invlaid inputs
    reset()
    output = customtkinter.CTkLabel(master=output_frame, text="You need to enter a number in both entry boxes.\nYou can search up to 365 days ago.")
    output.grid(row=0, column=0, pady=10, padx=10)

#click graph
def graph():
  try:
    #get current theme and set it to the graph
    #apperance_mode = customtkinter.get_appearance_mode()
    #if apperance_mode == "Dark":
    #  fc.draw_graph(value, s_currency_1, s_currency_2, True)
    #else:
    #  fc.draw_graph(value, s_currency_1, s_currency_2)

    #functiom from find_currency
     #this functions draws a graph in a new window
    fc.draw_graph(value, s_currency_1, s_currency_2)
    graph_button.configure(state="disabled") #turning off the draw graph bottun


  except Exception as e:
    #not needed if the graph bottun is disabled before converison
    print(e)#for debuggin
    output = customtkinter.CTkLabel(master=output_frame, text="You need to convert first.")
    output.grid(row=0, column=0, pady=10, padx=10)

#click reset
def reset():
  #everything is set to default
  global currency_1
  global currency_2
  global output
  output.destroy()
  output = customtkinter.CTkLabel(master=output_frame, text="The results will\nshow here")
  output.grid(row=0, column=0, pady=10, padx=10)
  e1.delete(0, END)
  e2.delete(0, END)
  currency_1 = "Euro"
  currency_2 = "United States Dollar"

  s_currency_1 = ""
  s_currency_2 = ""
  history_conv = 0
  value = 0

#click switch currency
def switch():
  #menu1 and menu2 selection switch places
  global currency_1
  global currency_2
  currency_1 = optionmenu_1.get()
  currency_2 = optionmenu_2.get()
  temp_currrency = currency_1 #temp variable
  currency_1 = currency_2
  currency_2 = temp_currrency
  optionmenu_1.set(currency_1)
  optionmenu_2.set(currency_2)

#change apperance mode
#switch on left = light, on right = dark
switch_var_1 = customtkinter.StringVar(value="left")

def to_light():
  customtkinter.set_appearance_mode("light")
def to_dark():
  customtkinter.set_appearance_mode("dark")

#switch for apperance mode events
def switch_1_event():
  value = switch_var_1.get()
  if value == "left":
    to_dark()
  elif value == "right":
    to_light()
  else:
    pass

#entry box for value
entry1_label = customtkinter.CTkLabel(master=root, text="Enter value in known currency:")
entry1_label.grid(row=0, column=0, columnspan=9)
e1 = customtkinter.CTkEntry(master=root, placeholder_text="", width=100)
e1.grid(row=1, column=0, columnspan=9)

#drop down menu 1
menu1_label = customtkinter.CTkLabel(master=root, text="Select currency to convert from:")
menu1_label.grid(row=2, column=0, columnspan=9)

optionmenu_1 = customtkinter.CTkOptionMenu(root, values= [*asd_full_name])
optionmenu_1.grid(row=3, column=0, columnspan=9)
optionmenu_1.set("Euro")

#drop down menu 2
menu2_label = customtkinter.CTkLabel(master=root, text="Select currency to convert to:")
menu2_label.grid(row=4, column=0, columnspan=9)

optionmenu_2 = customtkinter.CTkOptionMenu(root, values= [*asd_full_name])
optionmenu_2.grid(row=5, column=0, columnspan=9)
optionmenu_2.set("United States Dollar")

#entry box for days ago
entry2_label = customtkinter.CTkLabel(master=root, text="Use conversion rate from x days ago:")
entry2_label.grid(row=6, column=0, columnspan=9)
e2 = customtkinter.CTkEntry(master=root, placeholder_text="0", width=100)
e2.grid(row=7, column=0, columnspan=9)

#switch currency button
switch_text = customtkinter.CTkLabel(master=root, text="Switch 2 selected currencies")
switch_text.grid(row=8, column=0, columnspan=9)
switch_button = customtkinter.CTkButton(master=root, command=switch, text="Switch", width=100)  
switch_button.grid(row=9, column=0, columnspan=9)

#switch for appernace mode
s1_label = customtkinter.CTkLabel(master=root, text="Apperance mode:")
s1_label.grid(row=15, column=0, columnspan=9)
switch_1 = customtkinter.CTkSwitch(master=root, text="", command=switch_1_event, 
    variable=switch_var_1,onvalue="right",offvalue="left", width=50)
switch_1.grid(row=16, column=0, columnspan=9)

#buttons
bottun_row = 13 #most bottuns are in this row

convert_button = customtkinter.CTkButton(master=root, command=convert, text="Convert", width=100)  
convert_button.grid(row=bottun_row, column=1)

reset_button = customtkinter.CTkButton(master=root, command=reset, text="Reset", width=100)  
reset_button.grid(row=bottun_row, column=5)

quit_button = customtkinter.CTkButton(master=root, command=root.quit, text="Exit", width=100)  
quit_button.grid(row=bottun_row, column=7)

graph_button = customtkinter.CTkButton(master=root, command=graph, text="Show graph", width=100, state="disabled")  
graph_button.grid(row=bottun_row, column=3)

#output frame
output_frame = customtkinter.CTkFrame(master=root, width=400, height=50, corner_radius=10)
output_frame.grid(row=11, column=0, columnspan=9)
global output
output = customtkinter.CTkLabel(master=output_frame, text="The results will\nshow here")
output.grid(row=0, column=0, pady=10, padx=10)

#empty columns for visual
empty_col1 = customtkinter.CTkLabel(master=root, text="", width=20)
empty_col1.grid(row=bottun_row, column=0)
empty_col2 = customtkinter.CTkLabel(master=root, text="", width=20)
empty_col2.grid(row=bottun_row, column=2)
empty_col3 = customtkinter.CTkLabel(master=root, text="", width=20)
empty_col3.grid(row=bottun_row, column=4)
empty_col4 = customtkinter.CTkLabel(master=root, text="", width=20)
empty_col4.grid(row=bottun_row, column=6)
empty_col5 = customtkinter.CTkLabel(master=root, text="", width=20)
empty_col5.grid(row=bottun_row, column=8)

#empty rows for visual
empty_row1 = customtkinter.CTkLabel(master=root, text="")
empty_row2 = customtkinter.CTkLabel(master=root, text="")
empty_row3 = customtkinter.CTkLabel(master=root, text="")
empty_row1.grid(row=10, column=0, columnspan=9)
empty_row2.grid(row=12, column=0, columnspan=9)
empty_row3.grid(row=14, column=0, columnspan=9)

root.mainloop()