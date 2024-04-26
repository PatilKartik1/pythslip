''' Write a program which prints Fibonacci series of a number'''


# Python program to print Fibonacci series of a number

def fibonacci(n):
    # Initialize the first two terms of the Fibonacci sequence
    fib_sequence = [0, 1]
    
    # Generate Fibonacci sequence up to n terms
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    
    return fib_sequence

# Input the number of terms for Fibonacci series
num_terms = int(input("Enter the number of terms for Fibonacci series: "))

# Print Fibonacci series up to num_terms
print("Fibonacci series up to {} terms:".format(num_terms))
print(fibonacci(num_terms))
