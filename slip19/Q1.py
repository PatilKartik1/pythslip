''' Write a Python program to calculate the average of numbers in a given list. '''


# Function to calculate the average of numbers in a list
def calculate_average(numbers):
    total = sum(numbers)  # Calculate the sum of numbers in the list
    average = total / len(numbers)  # Calculate the average
    return average

# Main function to accept user input and display the average
def main():
    numbers = []  # Initialize an empty list to store numbers

    # Accept user input for the list of numbers
    n = int(input("Enter the number of elements in the list: "))
    print("Enter the numbers:")
    for i in range(n):
        num = float(input())
        numbers.append(num)

    # Calculate the average using the function
    avg = calculate_average(numbers)

    # Display the average
    print("Average of the numbers:", avg)

# Execute the main function
if __name__ == "__main__":
    main()
