def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

n1=eval(input("Enter first number: "))
n2=eval(input("Enter second number: "))
while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("Enter choice (1/2/3/4/5): ")
    
    if choice == '1':
        print(n1 ,"+", n2 ,"=", add(n1, n2))
    elif choice == '2':
        print(f"{n1} - {n2} = {subtract(n1, n2)}")
    elif choice == '3':
        print(f"{n1} * {n2} = {multiply(n1, n2)}")
    elif choice == '4':
        print(f"{n1} / {n2} = {divide(n1, n2)}")
    elif choice == '5':
        break
    else:
        print("Invalid input")