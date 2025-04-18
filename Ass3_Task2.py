import math


number = float(input("Enter a number: "))


if number <= 0:
    print("Natural logarithm is not defined for zero or negative numbers.")
else:
    square_root = math.sqrt(number)
    natural_log = math.log(number)
    sine_value = math.sin(number) 

  
    print(f"\nResults for the number {number}:")
    print(f"Square root: {square_root}")
    print(f"Natural logarithm (base e): {natural_log}")
    print(f"Sine (in radians): {sine_value}")
