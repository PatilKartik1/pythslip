# Write a Python function to check whether a number is in a given range.

def in_range(num, start, end):
    
    return start <= num <= end
# Example usage:
num = 10
start = 5
end = 15
if in_range(num, start, end):
    print(f"{num} is in the range [{start}, {end}]")
else:
    print(f"{num} is not in the range [{start}, {end}]")
