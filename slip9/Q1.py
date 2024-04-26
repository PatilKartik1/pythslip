'''Write a Python program to create a tuple using two different tuples. '''


def create_tuple(tuple1, tuple2):
    """
    Function to create a tuple using two different tuples.

    Args:
    tuple1 (tuple): The first tuple.
    tuple2 (tuple): The second tuple.

    Returns:
    tuple: The concatenated tuple containing elements from both input tuples.
    """
    return tuple1 + tuple2

# Two different tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
# Call the function and print the result
print("Concatenated Tuple:", create_tuple(tuple1, tuple2))
