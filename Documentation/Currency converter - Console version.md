# Currency converter - Console version

-------------------------
## *Contents:*

### Project Description
### Modules and libraries
### Detailed overview
### Inspiration and notes
--------------------------

## *1. Project Description:*
- Currency converter - Console version is a console based application for Windows developed in Python programming language.
- It brings a real currency exchange right to your Windows console, enabeling the user to see conversion rates for all available currencies.
- Apart from just converting a desired amount of chosen currency into another, it also offers to provide the user with historical data.
- To better understand the data provided, one can choose to view it as a graph, which would pop up in a seperate window.
- The app features a simple menu which prompts the user to select exactly what they need, after which they are instructed to input the needed information.
- It has an online, but also a data saving offline mode, curtosy to our big up-to-date local databases which are regularly optimized.
- Being console based, the program is highly efficient and light, especially when using local data.
- Apart from this console based version, we offer the same program as a desktop application featuring a modern GUI which some users may prefer.
- In the near future, we plan to develop a web version as well. Together with every other GMAZ project, it will be available for our users for free on official GMAZ website.

-------------------------


## *2. Modules and libraries:*
### **MatPlotLib**
- Used for data visualisation for both console and GUI version of the program.
- It takes in historical data for desired conversion rates during a time interval which the user inputs, and outputs a simple, but intuitive graphical representation.
- As a part of code optimization, which we take seriously, it is only used if the user chooses to do so.

### **Datetime**
- Used for getting current and historical dates and time. 
- Apart from providing the user with info, it is also used to correctly sort data both when using online and offline modes.

### **Requests**
- Used for sending requests to the exchange API from which we gather our data.
- Considering it is the main chokepoint for code exicution, it's crucial that we use it as little as possible.
- When in offline mode, it's obviouslly not used, which makes up for the performance gains when using the program offline.

### **Pandas** 
- Used only for development purposes because the data which the user sees is sorted and cleaned manually.
- Enables us to better understand the data we pull from the exchange API when making changes and improvements.
- To better optimize the code, this does not execute when regular users use the program.

-------------------------

## *3. Detailed overview:*
### **User view**
- When they run the application user will see a CommandPrompt window open.
- Inside they will see a customized menu where they will be prompted with input dialogs.
- <img width="430" alt="First Menu" src="https://user-images.githubusercontent.com/93053179/184852735-d0a016fc-136a-470c-a48a-0a7e75a0ea5c.PNG">
- Afrer the user enters a valid input, the program will ask for further info, like the need for historical data and data visualisation.
- <img width="504" alt="menu screen 2" src="https://user-images.githubusercontent.com/93053179/184853800-38b02679-10f1-49bc-b9fb-98870498dd2a.PNG">
- Then, if the user asks for a graph to better understand the data, custom function will be called and graph will display in a new window.
- <img width="458" alt="graph" src="https://user-images.githubusercontent.com/93053179/184854474-95f3e18d-107e-40de-809a-638d5d285f76.PNG">
- If not, the program will finish up and ask the use whether they would like to go again or exit.


### **Code analysis**
**Main.py file analysis**
- Example to be continued
```python

#importing needed modules
import find_currency as fc
from unit_testing import GenericError, InputError, WrongInputError
from currencies_data import all_currencies_dict as asd
import matplotlib.pyplot as plt

#sort imported data
asd_short = [n for n in asd.keys()]
asd_full_name = [n for n in asd.values()]

```
- Something else...
------------------------

## *4. Inspiration and notes:*
- This was our first project together as GMAZ.
- We chose a currency converter as our first project because we wanted to refresh our knowledge in big data and database manipulation while also learning to work as a team more efficiently.
- Apart from that, the need to get the live data from the internet made us learn how to do so efficiently, which will come in handy in future projects.
- Also, we noticed that Windows didn't provide any similar features by default on their platform so it was an easy choice.

-------------------------
***Copyright GMAZ.org***
