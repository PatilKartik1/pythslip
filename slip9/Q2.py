''' Write a Python program to sort (ascending and descending) a dictionary by value.'''


def sort_dictionary_by_value(dictionary, ascending=True):
    """
    Function to sort a dictionary by value in ascending or descending order.

    Args:
    dictionary (dict): The input dictionary to be sorted.
    ascending (bool, optional): Whether to sort in ascending order. Defaults to True.

    Returns:
    dict: The sorted dictionary.
    """
    # Sort the dictionary by value
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=not ascending))
    return sorted_dict

# Sample dictionary
sample_dict = {'a': 3, 'b': 1, 'c': 2}
# Sort in ascending order
ascending_sorted = sort_dictionary_by_value(sample_dict, ascending=True)
print("Ascending Order:", ascending_sorted)
# Sort in descending order
descending_sorted = sort_dictionary_by_value(sample_dict, ascending=False)
print("Descending Order:", descending_sorted)
