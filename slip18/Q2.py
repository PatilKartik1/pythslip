''' Write a Python program to accept n elements in a set and find the length of a set, maximum, 
minimum value and the sum of values in a set. (Don’t use built-in function) '''


# Function to find the length of a set
def find_length(s):
    length = 0
    for _ in s:
        length += 1
    return length

# Function to find the maximum value in a set
def find_maximum(s):
    max_val = None
    for num in s:
        if max_val is None or num > max_val:
            max_val = num
    return max_val

# Function to find the minimum value in a set
def find_minimum(s):
    min_val = None
    for num in s:
        if min_val is None or num < min_val:
            min_val = num
    return min_val

# Function to find the sum of values in a set
def find_sum(s):
    total = 0
    for num in s:
        total += num
    return total

# Main function
def main():
    n = int(input("Enter the number of elements in the set: "))
    elements = set()

    print("Enter the elements:")
    for _ in range(n):
        element = int(input())
        elements.add(element)

    print("Length of the set:", find_length(elements))
    print("Maximum value in the set:", find_maximum(elements))
    print("Minimum value in the set:", find_minimum(elements))
    print("Sum of values in the set:", find_sum(elements))

# Execute the main function
if __name__ == "__main__":
    main()
