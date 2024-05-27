from scipy.integrate import quad
from sympy import sympify, symbols, lambdify
import os

while True:
    # Get user input for the function to be integrated
    fx = input("Enter the function to be integrated: ")
    x = symbols('x')
    if fx[0].isdigit():  # Check if the first character is a digit
        fx = fx[0] + '*' + fx[1:]  # Add a multiplication sign after the integer coefficient
    f = lambdify(x, sympify(fx))

    # Get user inputs for the integration limits
    a = float(input("Enter the lower limit of integration: "))
    b = float(input("Enter the upper limit of integration: "))

    # Calculate the definite integral using user inputs
    result, error = quad(f, a, b)
    result = round(result, 2)   # Round the result to 2 decimal places

    print("The definite integral of the function is:", result)

    # Ask the user if they want to restart
    choice = input("\nPress Enter to restart:").lower()
    if choice != '':
        break
    os.system('cls' if os.name == 'nt' else 'clear')
