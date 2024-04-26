'''Write a Python function to get a string made of the first 2 and the last 2 chars from a given 
string. If the string length is less than 2, it return empty string. 
Sample String: 'General12' Expected Result: 'Ge12' 
Sample String: 'Ka' Expected Result: 'KaKa' 
Sample String: ' K' Expected Result: Empty String '''



def get_modified_string(s):
    # Check if the length of the string is less than 2
    if len(s) < 2:
        return ""  # Return empty string if length is less than 2
    else:
        # Concatenate the first 2 chars and the last 2 chars of the string
        modified_string = s[:2] + s[-2:]
        return modified_string

# Test cases
sample_strings = ['General12', 'Ka', ' K']
for string in sample_strings:
    print(f"Sample String: '{string}' Expected Result: '{get_modified_string(string)}'")
