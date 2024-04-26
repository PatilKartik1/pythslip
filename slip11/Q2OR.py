''' Write a Python program to accept n numbers in list. Find average of list and sort it in 
descending order.'''


# Python program to accept n numbers in list, find the average, and sort it in descending order

def main():
    # Input the number of elements
    n = int(input("Enter the number of elements: "))
    
    # Input the elements into a list
    numbers = []
    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    
    # Calculate the average of the list
    average = sum(numbers) / n
    
    # Sort the list in descending order
    numbers.sort(reverse=True)
    
    # Display the average and sorted list
    print(f"Average of the list: {average}")
    print("Sorted list in descending order:", numbers)

if __name__ == "__main__":
    main()
