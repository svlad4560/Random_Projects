from tkinter import *


grwoth_rate = float(input("Give me the growth rate in decimal form: " ))
print (grwoth_rate)

rr = float(input("Give me a required rate in decimal form: " ))
print (rr)

dividend = float(input("Give me a dividend in decimal form: " ))
print (dividend)

def find_purchase_price(grwoth_rate, rr, dividend):
    e.insert(0, dividend/(rr-grwoth_rate))




root = Tk()
root.title('Fin homework claculator')

e = Entry(root, width=35, borderwidth=5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def find_purchase_price(grwoth_rate, rr, dividend):
    e.insert(0, dividend/(rr-grwoth_rate))

requiered_stock_price = Button(root, text="Click for required purchase price", padx=40, pady=20, command=lambda: find_purchase_price(grwoth_rate, rr, dividend))
current_dividend = Button(root, text="Click for current dividend")


requiered_stock_price.grid(row=1, column=1)

root.mainloop()
