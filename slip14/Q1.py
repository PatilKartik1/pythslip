''' Write a Python program to create a tuple of n numbers and print maximum, minimum, and 
sum of elements in a tuple. '''


# Python program to create a tuple of n numbers and print maximum, minimum, and sum of elements in a tuple

def tuple_operations(numbers):
    # Convert the input list of numbers to a tuple
    num_tuple = tuple(numbers)
    
    # Calculate maximum, minimum, and sum of elements in the tuple
    max_num = max(num_tuple)
    min_num = min(num_tuple)
    sum_num = sum(num_tuple)
    
    # Print the results
    print("Maximum:", max_num)
    print("Minimum:", min_num)
    print("Sum:", sum_num)

# Input list of numbers
numbers = [int(x) for x in input("Enter the numbers separated by space: ").split()]

# Perform tuple operations
tuple_operations(numbers)
