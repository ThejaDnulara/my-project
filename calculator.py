import math  

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def exponentiate(x, y):  
    return x ** y

def modulus(x, y):  
    if y != 0:
        return x % y
    else:
        return "Error! Modulus by zero."

def square_root(x):  
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error! Square root of negative number."

def calculator():
    print("Welcome to the Enhanced Calculator!")  
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")  
    print("6. Modulus")  
    print("7. Square Root")  

    while True:  
        choice = input("Enter choice(1/2/3/4/5/6/7): ")

        if choice in ('1', '2', '3', '4', '5', '6', '7'):
            try:  
                if choice == '7':  
                    num1 = float(input("Enter number: "))
                    print(f"Square root of {num1} = {square_root(num1)}")
                else:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    if choice == '1':
                        print(f"{num1} + {num2} = {add(num1, num2)}")
                    elif choice == '2':
                        print(f"{num1} - {num2} = {subtract(num1, num2)}")
                    elif choice == '3':
                        print(f"{num1} * {num2} = {multiply(num1, num2)}")
                    elif choice == '4':
                        print(f"{num1} / {num2} = {divide(num1, num2)}")
                    elif choice == '5':  # New: Handling exponentiation
                        print(f"{num1} ^ {num2} = {exponentiate(num1, num2)}")
                    elif choice == '6':  # New: Handling modulus
                        print(f"{num1} % {num2} = {modulus(num1, num2)}")
            
            except ValueError:  # New: Exception for invalid numeric input
                print("Invalid input! Please enter a numeric value.")
            
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                print("Thank you for using the calculator. Goodbye!")
                break
        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    calculator()
