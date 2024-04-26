'''Write a program to display following pattern.
1 2 3 4 
1 2 3  
1 2   
1  '''



# Define the number of rows for the pattern
rows = 4

# Iterate through each row
for i in range(rows, 0, -1):
    # Print numbers from 1 to (rows - i + 1) in each row
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # Move to the next line after each row
