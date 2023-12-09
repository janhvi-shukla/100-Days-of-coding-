# Define a function called smallest_num_in_list that takes a list 'list' as input
def smallest_num_in_list(list):
    # Initialize a variable 'min' with the first element of the input list as the initial minimum
    min = list[0]
    # Iterate through each element 'a' in the input list 'list'
    for a in list:
        # Check if the current element 'a' is smaller than the current minimum 'min'
        if a < min:
            # If 'a' is smaller, update the minimum 'min' to 'a'
            min = a
    # Return the final minimum value in the list
    return min

# Call the smallest_num_in_list function with the list [1, 2, -8, 0] as input and print the result
print(smallest_num_in_list([1, 2, -8, 0]))