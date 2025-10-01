unit = input("Is this temparature in celcius or Fahrnheit (C/F): ")

temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 12, 1)
    print(f"The temparature in Fahrenheit is: {temp} F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temparature in Fahrenheit is: {temp} C")
else:
    print(f"{unit} is an invalid unit of measurement")
