import requests
import pprint
from tkinter import *
import pandas as pd

gui = Tk(className = "Fundamentals")
gui.geometry("1200x750")
stock_entry = Entry(gui,width = 35, borderwidth= 10)
stock_entry.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def search():
    global last
    searched_stock = stock_entry.get()

    url ="https://financialmodelingprep.com/api/v3/profile/"+searched_stock+"?apikey=2ead9f70179604e6f27f2a8fe3ffcf4a"
    data = requests.get(url).json()
    data_pd = pd.DataFrame(data)

    last_price = int(data_pd["price"])
    dcf = int(data_pd["dcf"])

    toplevel = Toplevel()
    if last_price > dcf :
        last = Label(gui,text=last_price, height = 0, width=50, bg = "green")
    else:
        last = Label(gui,text=last_price, height = 0, width=50, bg = "Red")
    last.grid(row=50, column=25)
def clear():
    stock_entry.delete(0, END)
    last.destroy()


search_button = Button(gui, text="search",command = search)
search_button.grid(row = 10, column = 10)
clear_button = Button(gui, text="clear search",command = clear)
clear_button.grid(row = 11, column = 10)


gui.mainloop()
