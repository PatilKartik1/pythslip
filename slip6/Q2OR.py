''' Write a Python program to display occurrence of the elements in the tuple, which appears 
more than 2 times. '''



def display_occurrences(tup):
    """
    Display the occurrences of elements in the tuple that appear more than 2 times.

    Args:
    tup (tuple): The input tuple.
    """
    # Create a dictionary to store the count of each element in the tuple
    count_dict = {}
    
    # Count the occurrences of each element in the tuple
    for elem in tup:
        if elem in count_dict:
            count_dict[elem] += 1
        else:
            count_dict[elem] = 1
    
    # Display elements with occurrences more than 2 times
    for key, value in count_dict.items():
        if value > 2:
            print(f"{key}: {value} times")

# Sample tuple
sample_tuple = (1, 2, 3, 4, 2, 2, 3, 3, 3, 5, 5)

# Display occurrences of elements appearing more than 2 times
display_occurrences(sample_tuple)
