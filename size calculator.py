from tkinter import *
import math
gui = Tk(className = "Fundamentals")

gui.geometry("1200x750")
stock_entry = Entry(gui,width = 35, borderwidth= 10)
stock_entry.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
intraday_stop = 100


def add_stop():
    return

def add_risk():
    global true_dollar_value
    intraday_risk_percent = stock_entry.get()
    true_dollar_value = intraday_risk_percent * intraday_stop

def add_trading_risk():
    global trading_risk
    trading_risk = stock_entry.get()

def calculate():
    value = true_dollar_value/trading_risk
    values = []
    values.append(value)

    display = Label(gui, text = values ,row = 1, column = 0)
    display.grid()



final_value = Button(gui, text='calculate',command = calculate)
final_value.grid(row = 0, column = 3)
intraday_risk_button = Button(gui, text='intraday risk',command = add_risk)
intraday_risk_button.grid(row = 2, column = 3)
risk_button = Button(gui, text='trading risk',command = add_trading_risk)
risk_button.grid(row = 3, column = 3)


gui.mainloop()


intraday_stop = 100
risk = .30
intraday_risk = .25
potential_loss = intraday_risk*intraday_stop
print("Size should be: " + str(math.floor(potential_loss/risk)))
