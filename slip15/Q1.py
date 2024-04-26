'''Write a python program to check if a string is a Palindrome or not. '''



def is_palindrome(s):
    return s == s[::-1]

# Test the palindrome function
test_cases = ["radar", "level", "hello", "12321", "python"]
for test_case in test_cases:
    if is_palindrome(test_case):
        print(f'"{test_case}" is a palindrome.')
    else:
        print(f'"{test_case}" is not a palindrome.')

# Output:
# "radar" is a palindrome.
# "level" is a palindrome.
# "hello" is not a palindrome.
# "12321" is a palindrome.
# "python" is not a palindrome.
