number1 = float(input("Веддіть перше число:"))
deia = input("Веддіть знак: ")
number2 = float(input("Веддіть друге число:"))

if deia == '+':
    print(number1 + number2)
elif deia == '-':
    print(number1 - number2)
elif deia == '*':
    print(number1 * number2)
elif deia == '/':
    print(number1 / number2)
else:
    print("дія не можлива")