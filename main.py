# Define a function named 'fibonacci' that takes an argument 'num'
def fibonacci(num):
    # Base case: If 'num' is less than 2, return 'num'
    if num < 2:
        return num
    else:
        # Recursive case: Calculate the Fibonacci sequence using recursion
        return fibonacci(num-1) + fibonacci(num-2)

# Print the 7th Fibonacci number
print(fibonacci(7))
