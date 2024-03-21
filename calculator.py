def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def modulo(x, y):
    return x %y


print("CALCULATOR MENU:")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
print("5.MODULO")

while True:
    
    choice = input("ENTER YOUR CHOICE: =(1/2/3/4/5) ")

    if choice in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("ENTER FIRST NUMBER: ="))
            num2 = float(input("ENTER SECOND NUMBER: ="))
        except ValueError:
            print("INVALID INPUT, PLEASE ENTER A NUMBER.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        elif choice=="5":
            print(num1,"%",num2,"=",modulo(num1,num2))
            
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        Print("INVALID INPUT")
