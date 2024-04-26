''' Write a Python program to check if a given key already exists in a dictionary. If key exists 
replace with another key/value pair. '''


def replace_key(dictionary, key, new_key, new_value):
    """
    Check if a given key already exists in a dictionary. If the key exists, replace it with another key/value pair.
    
    Parameters:
        dictionary (dict): The dictionary to check and update.
        key: The key to check.
        new_key: The new key to replace the existing one.
        new_value: The new value corresponding to the new key.
    
    Returns:
        dict: The updated dictionary.
    """
    if key in dictionary:
        dictionary[new_key] = new_value
        del dictionary[key]
    return dictionary

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_replace = 'b'
new_key = 'x'
new_value = 10
updated_dict = replace_key(my_dict, key_to_replace, new_key, new_value)
print("Updated Dictionary:", updated_dict)
