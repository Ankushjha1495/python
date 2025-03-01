# 1 inches = 2.54cm
def converter(inches):
    return inches*2.54
n = int(input("Enter the inches:"))
print(f"The value of {n} inches in Centimeter is {converter(n)}")

