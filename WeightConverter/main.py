weight = float(input("Enter your weight here: "))

unit = input("Enter either (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"The new weight is {round(weight, 3)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"The new weight is {round(weight, 3)} {unit}")
else:
    print(f"{unit} is an Invalid unit")
