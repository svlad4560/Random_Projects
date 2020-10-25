topping = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', ' mushrooms']
prices = [2,6,1,3,2,7,2]

num_pizzas= len(topping)
pizzas = list(zip(prices, topping))

# this makes is sort by price from least to greatest
pizzas.sort()

# this prints the cheapest which is the first in the list
cheapest_pizza = pizzas[0]

# this prints the last thing in the list
priciest_pizza = pizzas[-1]

# this prints the first 3 options
three_cheapest = pizzas[:3]


num_two_dollar_slices = prices.count(2)
#this prints 3 2 dollar prices
print(num_two_dollar_slices)

# why does this print 0? I would think that it should print 3 as well
num_of_two = pizzas.count(2)
print(num_of_two)

print(dir(topping))
print(dir(pizzas))
