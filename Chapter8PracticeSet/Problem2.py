# Formula for celcius into farenheit c = 5*(f-32)/9
def TempChanger(f):
    return 5*(f-32)/9
f = int(input("Enter the temperature in f: "))
print(round(TempChanger(f),2))
