print("Welcome to Python Pizzaria!")
size = input("What size pizza you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

spizza = 15
mpizza = 20
lpizza = 25
price_pepperoni_small = 2
price_pepperonis_med_or_large = 3
price_extra_cheese = 1
total_pizza_cost = 0

if size == "S":
    total_pizza_cost = 15
    if pepperoni == "Y":
        total_pizza_cost += 2
        if extra_cheese == "Y":
            total_pizza_cost += 1
elif size == "M":
    total_pizza_cost = 20
    if pepperoni == "Y":
        total_pizza_cost += 3
        if extra_cheese == "Y":
            total_pizza_cost += 1
elif size == "L":
    total_pizza_cost = 25
    if pepperoni == "Y":
        total_pizza_cost += 3
        if extra_cheese == "Y":
            total_pizza_cost += 1

print("Your price comes to " + str(total_pizza_cost))
