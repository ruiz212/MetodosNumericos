import sympy as sp

# Define the symbol (variable)
x = sp.symbols('x')

# Get the function input from the user as a string
user_function = input("Enter the function you want to expand (e.g., tan(x), sin(x), ln(1+x)): ")

# Convert the string into a symbolic expression
f = sp.sympify(user_function)

# Get user input for the number of terms (polynomial degree) and the central value
n = int(input("Enter the number of terms for the Taylor series: "))
a = float(input("Enter the central value (a) for the Taylor series: "))

# Compute the Taylor series using SymPy's series() function
taylor_series = sp.series(f, x, a, n)

# Simplify the Taylor series expression to make sure it's properly displayed
taylor_series = sp.simplify(taylor_series)

# Display the result
print(f"Taylor series of {user_function} around {a} up to {n} terms:")
print(taylor_series)

# Get user input for the specific value of x where they want to evaluate the approximation
x_value = float(input("Enter the value of x to evaluate the function and its Taylor series approximation: "))

# Evaluate the actual function at x_value
actual_value = f.subs(x, x_value)

# Evaluate the Taylor series approximation at x_value
taylor_approx_value = taylor_series.subs(x, x_value)

# Display both the actual value and the approximation
print(f"Actual value of {user_function} at x = {x_value}: {actual_value}")
print(f"Taylor series approximation at x = {x_value}: {taylor_approx_value}")