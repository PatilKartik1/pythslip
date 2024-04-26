''') Write a Python program which prints fibonacci series of a number. '''


def fibonacci(n):
    """
    Generate and print the Fibonacci series up to the nth term.
    
    Parameters:
        n (int): The number of terms in the Fibonacci series to generate.
    
    Returns:
        None
    """
    # Initialize the first two terms of the Fibonacci series
    first_term = 0
    second_term = 1
    
    # Print the first two terms (0 and 1)
    print(first_term, end=" ")
    print(second_term, end=" ")
    
    # Generate the remaining terms up to the nth term
    for _ in range(2, n):
        next_term = first_term + second_term
        print(next_term, end=" ")
        first_term = second_term
        second_term = next_term

# Test the function
n = int(input("Enter the number of terms in the Fibonacci series: "))
fibonacci(n)
