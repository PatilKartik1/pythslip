''' Write a Python program to remove special symbols/Punctuation from a given string.'''



import string

def remove_punctuation(input_string):
    # Create a translation table to map each punctuation character to None
    translation_table = str.maketrans('', '', string.punctuation)
    # Remove punctuation using translate() method with the translation table
    clean_string = input_string.translate(translation_table)
    return clean_string

# Example usage
input_string = "Hello! This is a sample string with punctuations!!"
cleaned_string = remove_punctuation(input_string)
print("Original String:", input_string)
print("String after removing punctuation:", cleaned_string)
