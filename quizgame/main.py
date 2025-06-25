foods = []
prices = []
Total = 0

while True:
    food = input("Enter the type of food here: ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter the price of items here: $"))
        print(f"You bought {food} for {price}")
        prices.append(price)
        foods.append(food)

for food in foods:
    print(food, end=" ")
print()
print()
for price in prices:
    Total += price
    print(Total)
