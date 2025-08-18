weight = float(input("Enter the weight: "))

unit = input("Enter the weight. (K or L)")


if unit == "K":
    weight = weight * 2.205
    unit = "L"
    print(f"The results are {round(weight, 1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "K"
    print(f"The results are {round(weight, 1)} {unit}")
else:
    print(f"{unit} was invalid")
