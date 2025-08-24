unit = input("Is this temparature in Celcius or Fahrenheit (C/F): ")
temp = float(input("Enter the temparature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(F"The temparature in Fahrenheit is {temp}F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(F"The temparature in Fahrenheit is {temp}c")
else:
    print(f"{unit} is an invalid unit of measurement")
