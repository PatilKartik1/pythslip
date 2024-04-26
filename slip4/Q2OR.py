'''Write a Python program to create a set with any 3 weekdays. Add single element to the set 
and print it. Add multiple elements and print the set.'''

# Create a set with any 3 weekdays
weekdays_set = {'Monday', 'Wednesday', 'Friday'}
print("Initial set of weekdays:", weekdays_set)

# Add a single element to the set
weekdays_set.add('Thursday')
print("Set after adding a single weekday:", weekdays_set)

# Add multiple elements to the set
weekdays_set.update(['Saturday', 'Sunday'])
print("Set after adding multiple weekdays:", weekdays_set)
