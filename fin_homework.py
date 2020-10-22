from tkinter import *


type_of_problem = str(input("""
What are you trying to do?
1: Find current stock price
2: Find current dividend
Please type '1' or '2' and hit enter
"""))


if type_of_problem == "1":

    grwoth_rate = float(input("Give me the growth rate in decimal form: " ))
    rr = float(input("Give me a required rate in decimal form: " ))
    dividend = float(input("Give me a dividend in decimal form: " ))

    root = Tk()
    root.title('Fin homework claculator')

    e = Entry(root, width=35, borderwidth=5)
    e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

    def find_purchase_price(grwoth_rate, rr, dividend):
        e.insert(0, dividend/(rr-grwoth_rate))

    requiered_stock_price = Button(root, text="Click for required purchase price", padx=40, pady=20, command=lambda: find_purchase_price(grwoth_rate, rr, dividend))
    requiered_stock_price.grid(row=1, column=1)

    root.mainloop()

if type_of_problem == "2":

    rr = float(input("Give me a required rate in decimal form: " ))
    grwoth_rate = .50 * rr
    current_stock_price = float(input('Give me the current stock price: '))

    root = Tk()
    root.title('Fin homework claculator')

    e = Entry(root, width=35, borderwidth=5)
    e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

    def find_dividend(grwoth_rate, rr, current_stock_price):
        e.insert(0, (current_stock_price* grwoth_rate)/(1+grwoth_rate))

    requiered_dividend = Button(root, text="Click for required dividend", padx=40, pady=20, command=lambda: find_dividend(grwoth_rate, rr, current_stock_price))
    requiered_dividend.grid(row=1, column=1)

    root.mainloop()
else:
    print('not valid choice')
