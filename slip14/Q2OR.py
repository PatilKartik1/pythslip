''' Write a Python program to define class to find validity of a string of parentheses, '(', ')', '{', 
'}', '[' and ']. These brackets must be in the correct order, for example "()" and "()[]{}" are valid 
but "[)", "({[)]" and "{{{" are invalid.'''


class ValidParentheses:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

# Test the ValidParentheses class
validator = ValidParentheses()
test_cases = ["()", "()[]{}", "[)", "({[)]", "{{{"]
for test_case in test_cases:
    if validator.isValid(test_case):
        print(f'"{test_case}" is valid.')
    else:
        print(f'"{test_case}" is invalid.')

# Output:
# "()"" is valid.
# "()[]{}" is valid.
# "[)" is invalid.
# "({[)]" is invalid.
# "{{{" is invalid.
