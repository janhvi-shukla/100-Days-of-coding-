# Define a function 'unique_sublists' that counts the number of unique sublists in 'input_list'
def unique_sublists(input_list):
    # Create an empty dictionary 'result' to store the sublists and their counts
    result = {}
    # Iterate through the sublists in 'input_list'
    for l in input_list:
        # Use a tuple representation of the sublist as a key to the 'result' dictionary
        # and append 1 to the list associated with that key
        result.setdefault(tuple(l), list()).append(1)
    # Iterate through the items in 'result' and replace the list of counts with their sum
    for a, b in result.items():
        result[a] = sum(b)
    return result

# Create a list 'list1' containing sublists of numbers
list1 = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'list1'
print(list1)
# Print a message indicating the number of unique sublists in the list
print("Number of unique lists of the said list:")
# Call the 'unique_sublists' function with 'list1' and print the result
print(unique_sublists(list1))

# Create a list 'color1' containing sublists of colors
color1 = [["green", "orange"], ["black"], ["green", "orange"], ["white"]]

# Print a message indicating the original list
print("\nOriginal list:")
# Print the contents of 'color1'
print(color1)
# Print a message indicating the number of unique sublists in the list
print("Number of unique lists of the said list:")
# Call the 'unique_sublists' function with 'color1' and print the result
print(unique_sublists(color1))
