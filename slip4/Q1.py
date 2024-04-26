''' Write a Python program to find the repeated items of a tuple. '''

def find_repeated_items(tuple_input):
    repeated_items = []
    for item in tuple_input:
        if tuple_input.count(item) > 1 and item not in repeated_items:
            repeated_items.append(item)
    return repeated_items

# Test the function
test_tuple = (1, 2, 3, 2, 4, 5, 6, 6, 7, 8, 8)
repeated_items = find_repeated_items(test_tuple)
print("Repeated items:", repeated_items)
