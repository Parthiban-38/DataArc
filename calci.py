def calculate(n1, n2, operation):
    if operation == '1':
        return n1 + n2
    elif operation == '2':
        return n1 - n2
    elif operation == '3':
        return n1 * n2
    elif operation == '4':
        if n2 == 0:
            return "Error! Division by zero."
        return n1 / n2
    else:
        return "Invalid operation"

try:
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
except ValueError:
    print("❌ Error! Please enter valid numeric values.")
          

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("Enter choice (1/2/3/4/5): ")
    
    if choice == '5':
        break
    result = calculate(n1, n2, choice)
    print("Result:", result)
