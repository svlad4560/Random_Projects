import requests
import pprint
from tkinter import *
import pandas as pd

stock = "ZM"
url = "https://financialmodelingprep.com/api/v3/profile/"+stock+"?apikey=2ead9f70179604e6f27f2a8fe3ffcf4a"
dcf_url ="https://financialmodelingprep.com/api/v3/historical-discounted-cash-flow/"+stock+"?period=quarter&apikey=2ead9f70179604e6f27f2a8fe3ffcf4a"
trading_stats_url = "https://financialmodelingprep.com/api/v3/profile/"+stock+"?apikey=2ead9f70179604e6f27f2a8fe3ffcf4a"
most_active = "https://financialmodelingprep.com/api/v3/actives?apikey=2ead9f70179604e6f27f2a8fe3ffcf4a"
api_key = "2ead9f70179604e6f27f2a8fe3ffcf4a"
data = requests.get(url).json()
active_data = requests.get(most_active).json()
# pprint.pprint(active_data)

# dcf_data = requests.get(dcf_url).json()
# pprint.pprint(dcf_data)

url ="https://financialmodelingprep.com/api/v3/profile/"+stock+"?apikey=2ead9f70179604e6f27f2a8fe3ffcf4a"
data = requests.get(url).json()
# data_pd = pd.DataFrame(data)

# last_price = int(data_pd["price"])
# dcf = int(data_pd["dcf"])

gui = Tk(className = "Fundamentals")

gui.geometry("1200x750")
stock_entry = Entry(gui,width = 35, borderwidth= 10)
stock_entry.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def add():
    global comparison
    comparison = []
    searched_stock = stock_entry.get()
    comparison.append(searched_stock)

def clear():
    stock_entry.delete(0, END)

def check_porfolio():
    display_list = []

    for stock in comparison:

        url ="https://financialmodelingprep.com/api/v3/profile/"+stock+"?apikey=2ead9f70179604e6f27f2a8fe3ffcf4a"
        data = requests.get(url).json()
        data_pd = pd.DataFrame(data)

        last_price = int(data_pd["price"])
        dcf = int(data_pd["dcf"])
        if last_price >= dcf:
            display_list.append(stock)

        global display

        display = Label(gui, text = display_list,height = 10, width = 25)
        display.grid()

def clear_dcf():
    display.destroy()


add_button = Button(gui, text="search",command = add)
add_button.grid(row = 10, column = 10)
clear_button = Button(gui, text="clear search",command = clear)
clear_button.grid(row = 11, column = 10)
check_porfolio_button = Button(gui, text="check porfolio",command = check_porfolio)
check_porfolio_button.grid(row = 12, column = 10)
clear_dcf = Button(gui, text = "clear porfolio", command = clear_dcf)
clear_dcf.grid(row = 13, column =10)

gui.mainloop()
