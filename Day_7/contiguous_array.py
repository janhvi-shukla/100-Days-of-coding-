import sys
def findMaxLenght(nums):
    num=list(map(int,nums.split()))
    sum_index_map={0:-1}
    max_lenght=0
    current_sum=0
    for index,num in enumerate(nums):
        current_sum+=1 if num==1 else -1
        if current_sum in sum_index_map:
            max_lenght=max(max_lenght,index - sum_index_map[current_sum])
        else:
            sum_index_map[current_sum]=index
            
    return max_lenght
nums= input( )
print (findMaxLenght(nums))
                          
