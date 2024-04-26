''' Write a Sequential search function which searches an item in a sorted list. The function 
should return the index of element to be searched in the list. '''

def sequential_search(sorted_list, target):
    """
    Perform a sequential search on a sorted list to find the target element.
    
    Parameters:
        sorted_list (list): A sorted list of elements.
        target: The element to search for in the list.
    
    Returns:
        int: The index of the target element in the list if found, otherwise -1.
    """
    for i in range(len(sorted_list)):
        if sorted_list[i] == target:
            return i
        elif sorted_list[i] > target:
            # Since the list is sorted, if the current element is greater than the target,
            # it means the target does not exist in the list.
            return -1
    return -1  # Target not found

# Test the sequential_search function
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13
index = sequential_search(sorted_list, target)
if index != -1:
    print(f"The target element {target} is found at index {index}.")
else:
    print(f"The target element {target} is not found in the list.")
