
from itertools import groupby

# initializing list
test_list = [1, 3, 5, 1, 3, 2, 5, 4, 2]

# printing original list
print("The original list : " + str(test_list))

res = [list(val) for key, val in groupby(sorted(test_list))]

# printing result
print("Matrix after grouping : " + str(res))
