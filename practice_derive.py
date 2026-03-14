import sympy as sp

# Define the symbol (variable)
x = sp.symbols('x')

# Get the function input from the user as a string
user_function = input("Enter the function you want to differentiate (e.g., tan(x), sin(x), ln(1+x)): ")

# Convert the string into a symbolic expression
f = sp.sympify(user_function)

# Get user input for the number of derivatives
n = int(input("Enter the number of derivatives you want to compute: "))
list_derivatives = []
# Compute the derivatives and display each one
derivative = f
for i in range(1, n + 1):
    derivative = sp.diff(derivative, x)
    list_derivatives.append(derivative)

 
 
# Print the derivatives
for i, d in enumerate(list_derivatives, start=1):
    print(f"The {i}-th derivative of {f} is: {d}")   
    

GetDerivative = int(input("Enter the order of the derivative you want to retrieve: "))
if 1 <= GetDerivative <= n:
    print(f"The {GetDerivative}-th derivative of {f} is: {list_derivatives[GetDerivative - 1]}")
else:
    print("Invalid input. Please enter a number between 1 and", n)