''' Write a function to calculate the sum of numbers from 0 to n. '''

def sum_of_numbers(n):
    """
    Calculate the sum of numbers from 0 to n.

    Args:
    n (int): The upper limit of the range.

    Returns:
    int: The sum of numbers from 0 to n.
    """
    return n * (n + 1) // 2

# Example usage:
n = 10
result = sum_of_numbers(n)
print("The sum of numbers from 0 to", n, "is:", result)
