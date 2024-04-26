''' Write a Python program to reverse a given number. '''


# Python program to reverse a given number

def reverse_number(num):
    # Convert the number to a string and reverse it
    reversed_num = str(num)[::-1]
    # Convert the reversed string back to an integer
    reversed_num = int(reversed_num)
    return reversed_num

# Test the function
number = int(input("Enter a number to reverse: "))
reversed_number = reverse_number(number)
print("Reversed number:", reversed_number)
