#module imports
import requests #pip install requests
import datetime
import matplotlib.pyplot as plt

#set variables
today_time = datetime.datetime.now()
history_rates = []
history_rates_dates = []


#function definiton
def get_rates(amount, currency, converted_currency, number_of_days = 0):
  date_1y = (today_time - datetime.timedelta(days=1 * number_of_days))

  #sending request to the api
  url = f"https://api.exchangerate.host/timeseries"
  #setting parameters for receiving data
  payload_dict = {
                "base" : currency,
                "amount" : amount,
                "start_date" : date_1y.date(),
                "end_date" : today_time.date()
              }
  response = requests.get(url, params=payload_dict)
  #saving recieved data to a dictionary
  data_dict = response.json()

  #data storage
  currency_rate_history = {}
  rate_history_array = []

  #getting the data we need from the dictionary
  #"rates" is the key because api sends some other data exept the rates but we dont need it
  for item in data_dict["rates"]:
    current_date = item
    #we need to get the rates for the specific date which is the next key
    currency_rate = data_dict["rates"][item][converted_currency]

    #adding data to the local dictionary for later use
    currency_rate_history[current_date] = [currency_rate] 
    rate_history_array.append(currency_rate)


  #returning amount in selected currency and date of conversion rate
  dates = [n for n in currency_rate_history.keys()]
  date_of_conversion = dates[0]
  wanted_currency_rate = currency_rate_history.get(date_of_conversion)[0]
  
  #clearing data reciving variables
  history_rates.clear()
  history_rates_dates.clear()
  
  #returning data
  history_rates.append(rate_history_array)
  dates = [n[5:] for n in dates]
  history_rates_dates.append(dates)
  return wanted_currency_rate, date_of_conversion



#drawing history graph using the list generated in the upper function
#needs to be ran after the get_rates when used outside of this scope
def draw_graph(amount, currency, converted_currency, dark_mode = False):

  #clearing previous graph
  plt.clf()

  #setting constant
  GMAZ_GREEN = "#16DB65"
  GMAZ_ORANGE = "#db7616"
  WHITE = "#FFFFFF"
  BLACK = "#000000"

  #setting graph style
  if dark_mode:
    plt.style.use("dark_background")
    marker_color = BLACK
  else:
    plt.style.use('ggplot')
    marker_color = WHITE

  try:
    #calculating needed data
    days_num = len(history_rates[0])
    avrg = sum(history_rates[0]) / days_num
    avrg_arr = [avrg for n in history_rates[0]]

    #define first subplot
    plt.plot(history_rates_dates[0], history_rates[0],
            color=GMAZ_GREEN, label="Daily Rate", linewidth=1.9,
            marker="o", markersize=3.8, markerfacecolor=marker_color,
            antialiased=True) #trendline

    #define second subplot
    plt.plot(history_rates_dates[0], avrg_arr, color=GMAZ_ORANGE, 
            label=f"Average of {days_num} days",
            linewidth=1.6, linestyle="--") #average line
    
    #name axis
    plt.ylabel(f"{amount} {currency} to {converted_currency}", fontname="Calibri", fontsize=14)
    plt.xlabel("Days", fontname="Calibri", fontsize=14)
    plt.title(f"Conversion rate diagram {currency}/{converted_currency}", fontname="Calibri", fontsize=16)

    #show the plot
    plt.legend(loc="best", frameon=True, shadow=True, fancybox=True)
    plt.tight_layout()
    plt.grid(linewidth=0.5, linestyle="--")
    plt.show()
    

  #if there is no data to draw or other errors raised
  except:
    print("Something went wrong!")