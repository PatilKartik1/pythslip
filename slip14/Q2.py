'''Write a Python program which accept an integer value ‘n’ and display all prime numbers 
till ‘n’.'''


# Python program to display all prime numbers up to 'n'

def is_prime(num):
    """Function to check if a number is prime"""
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def display_primes(n):
    """Function to display all prime numbers up to 'n'"""
    print("Prime numbers up to", n, "are:")
    for i in range(2, n + 1):
        if is_prime(i):
            print(i, end=" ")

# Accept the input from the user
n = int(input("Enter the value of 'n': "))

# Display prime numbers up to 'n'
display_primes(n)
