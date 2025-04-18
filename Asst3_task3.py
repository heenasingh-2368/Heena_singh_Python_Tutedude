
def factorial(n):
    if n < 0:
        return 
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


sample_number = 5
output = factorial(sample_number)
print(f"The factorial of {sample_number} is: {output}")
