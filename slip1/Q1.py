def in_range(num, start, end):
    """
    Check if the number `num` falls within the range [start, end].

    Parameters:
        num (int): The number to check.
        start (int): The start of the range (inclusive).
        end (int): The end of the range (inclusive).

    Returns:
        bool: True if `num` is within the range [start, end], False otherwise.
    """
    return start <= num <= end
# Example usage:
num = 10
start = 5
end = 15
if in_range(num, start, end):
    print(f"{num} is in the range [{start}, {end}]")
else:
    print(f"{num} is not in the range [{start}, {end}]")
