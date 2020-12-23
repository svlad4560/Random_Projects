from tkinter import *

# root = Tk()
# root.title('Fin homework claculator')
#
# e = Entry(root, width=35, borderwidth=5)
# e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

type_of_problem = str(input("""
What are you trying to do?
1: Find current stock price
2: Find current dividend
3: Find Payback Period
Please type '1' or '2' and hit enter
"""))
root = TK()
root.title('Fin homework claculator')
root.geometry('700x500')

if type_of_problem == "1":

    grwoth_rate = float(input("Give me the growth rate in decimal form: " ))
    rr = float(input("Give me a required rate in decimal form: " ))
    dividend = float(input("Give me a dividend in decimal form: " ))

    root = Tk()
    root.title('Fin homework claculator')
    root.geometry('700x500')

    e = Entry(root, width=35, borderwidth=5)
    e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

    def find_purchase_price(grwoth_rate, rr, dividend):
        e.insert(0, dividend/(rr-grwoth_rate))

    # def return_to_input():
    #     e.delete(0, END)
    #     input() we woudl need a loop in order to get back to the input screen

    requiered_stock_price = Button(root, text="Click for required purchase price", padx=40, pady=20, command=lambda: find_purchase_price(grwoth_rate, rr, dividend))
    requiered_stock_price.grid(row=1, column=1)

    root.mainloop()

if type_of_problem == "2":

    rr = float(input("Give me a required rate in decimal form: " ))
    grwoth_rate = .50 * rr
    current_stock_price = float(input('Give me the current stock price: '))

    def find_dividend(grwoth_rate, rr, current_stock_price):
        e.insert(0, (current_stock_price* grwoth_rate)/(1+grwoth_rate))

    requiered_dividend = Button(root, text="Click for required dividend", padx=40, pady=20, command=lambda: find_dividend(grwoth_rate, rr, current_stock_price))
    requiered_dividend.grid(row=1, column=1)

    root.mainloop()

if type_of_problem == "3":
    print("Enter Cash flow for each year")
    year0 = int(input("Year0: " ))
    year1 = int(input("Year1: " ))
    year2 = int(input("Year2: " ))
    year3 = int(input("Year3: " ))
    year4 = int(input("Year4: " ))

    def find_payback_period(year0,year1,year2,year3, year4):
        last_step = ((year0 - year1) - year2)- year3
        e.insert(0,3+(last_step/year4))

    paybackperiod = Button(root, text="click for payback period", padx=40, pady=20, command=lambda: find_payback_period(year0, year1, year2, year3, year4))
    paybackperiod.grid(row=1, column=1)

    root.mainloop()

else:
    print('not valid choice')
