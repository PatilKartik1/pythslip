''' Write a Python program to accept n numbers in list and remove duplicates from a list.'''



# Python program to accept n numbers in a list and remove duplicates

def remove_duplicates(input_list):
    # Create an empty list to store unique elements
    unique_list = []
    
    # Iterate through the input list
    for num in input_list:
        # Check if the element is not already in the unique list
        if num not in unique_list:
            # Append the element to the unique list
            unique_list.append(num)
    
    return unique_list

# Test the function
n = int(input("Enter the number of elements: "))
numbers = []

# Accept n numbers from the user
for i in range(n):
    numbers.append(int(input("Enter number {}: ".format(i + 1))))

# Remove duplicates from the list
result = remove_duplicates(numbers)
print("List after removing duplicates:", result)
