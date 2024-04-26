'''Write a Python program to display the following pattern (Floyd's triangle) 
For n=3 
1 
2 3 
4 5 6'''

def print_floyds_triangle(n):
    """
    Prints Floyd's Triangle pattern for the given number of rows 'n'.
    
    Parameters:
        n (int): The number of rows in Floyd's Triangle.
    """
    num = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()

# Displaying Floyd's Triangle for n = 3
print("Floyd's Triangle for n = 3:")
print_floyds_triangle(3) 
