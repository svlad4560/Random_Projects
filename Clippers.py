hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# this is a way to edit the list
new_prices = [price - 5 for price in prices]
# print(new_prices)


def find_ave(lista):
    total = 0
    for a in prices:
        total += a
    total_num = len(lista)
    average = total / total_num
    return average


def find_rev(last_week):
    for a in last_week:
        total_rev = 0
        total_rev += a
    return total_rev

print(find_ave(last_week))

# print(find_ave(prices))
