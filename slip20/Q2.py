''' Write a Python program which finds sum of digits of a number. [20 M] 
Example n=130 then output is 4 (1+3+0). '''


def sum_of_digits(number):
    # Convert the number to a string to iterate through its digits
    num_str = str(number)
    # Initialize a variable to store the sum of digits
    total_sum = 0
    # Iterate through each digit in the string
    for digit in num_str:
        # Convert the digit back to an integer and add it to the total sum
        total_sum += int(digit)
    # Return the total sum
    return total_sum

# Example usage
n = 130
result = sum_of_digits(n)
print(f"Sum of digits of {n}: {result} ({'+'.join(str(d) for d in map(int, str(n)))})")
