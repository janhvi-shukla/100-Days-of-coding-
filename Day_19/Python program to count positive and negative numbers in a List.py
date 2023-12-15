list1 = [-10, -21, -4, -45, -66, 93, 11]
 
pos_count, neg_count = 0, 0
num = 0
 
# using while loop
while(num < len(list1)):
 
    # checking condition
    if list1[num] >= 0:
        pos_count += 1
    else:
        neg_count += 1
 
    # increment num
    num += 1
 
print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", neg_count)
