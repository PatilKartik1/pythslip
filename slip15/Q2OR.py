''' Write a Python program which finds sum of digits of a number. [20 M] 
Example n=135 then output is 9 (1+3+5). '''


def sum_of_digits(n):
    """
    Calculate the sum of digits of a given number.
    
    Parameters:
        n (int): The number for which the sum of digits needs to be calculated.
    
    Returns:
        int: The sum of digits of the given number.
    """
    # Convert the number to a string to iterate through its digits
    digits = str(n)
    # Initialize the sum
    total_sum = 0
    # Iterate through each digit and add it to the sum
    for digit in digits:
        total_sum += int(digit)
    return total_sum

# Test the sum_of_digits function
n = 135
output = sum_of_digits(n)
print(f"The sum of digits of the number {n} is: {output} ({'+'.join(str(d) for d in str(n))})")
