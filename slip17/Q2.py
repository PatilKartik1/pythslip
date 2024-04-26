'''Write a Python program which accepts an integer value ‘n’ and display all prime 
numbers till ‘n’.'''



def is_prime(num):
    """
    Checks if a number is prime.
    
    Parameters:
        num (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def display_prime_numbers(n):
    """
    Displays all prime numbers up to 'n'.
    
    Parameters:
        n (int): The upper limit for prime numbers.
    """
    print("Prime numbers up to", n, "are:")
    for num in range(2, n + 1):
        if is_prime(num):
            print(num, end=" ")

# Accepting user input
n = int(input("Enter an integer value for 'n': "))
display_prime_numbers(n)
