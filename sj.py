num1 = int(input("Enter 1st num: "))
num2 = int(input("Enter 2nd num: "))

def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

print("Select an option:\n1. Add\n2. Subtract \n3. Multipy\n4. Divide")

option = 1

if option == 1:
    result = add(num1, num2)
    print(f"{num1} +  {num2} = {result}")

elif option == 2:
    result = subtract(num1, num2)
    print(f"{num1} -  {num2} = {result}")

elif option == 3:
    result = multiply(num1, num2)
    print(f"{num1} x  {num2} = {result}")

elif option == 4:
    result = divide(num1, num2)
    print(f"{num1} /  {num2} = {result}")

else:
    print("Invalid Input!")




