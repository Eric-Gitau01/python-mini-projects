# foods = []
# prices = []
# total = 0

# while True:
#     food = input("Enter a food to buy (q to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of a {food}: $"))
#         foods.append(food)
#         prices.append(price)

# print("-----YOUR CART -------")

# for food in foods:
#     print(food, end=" ")

import json

data = {
    "name": "Kasaongo W",
    "age": 65,
    "email": False,
    "is_active": False
}


with open("output.json", "w") as json_file:
    json.dump(data, json_file)


print("JSON data written")
