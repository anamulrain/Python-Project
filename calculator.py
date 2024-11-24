def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

def pow(x,y):
    return x ** y

def calculator():
    print("Welcome to My Calculator")
    print("Select Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power of")

    while True:
        choice = input("Enter choice (1/2/3/4/5) or 'q' to exit ")

        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2}  =  {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2}  =  {sub(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2}  =  {mul(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2}  =  {div(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ** {num2}  =  {pow(num1, num2)}")
        else:
            print("Invalid choice! Please select a valid operation.")
            

if __name__ == "__main__":
    calculator()