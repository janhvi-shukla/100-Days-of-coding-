
def findFreeinterval(arr, N):
	if N < 1:
		return
	
	# To store the set of free interval
	P = []
	arr.sort(key = lambda a:a[0])
	
	# Iterate over all the interval 
	for i in range(1, N):
		
		# Previous interval end 
		prevEnd = arr[i - 1][1]
		
		# Current interval start 
		currStart = arr[i][0]
		if prevEnd < currStart:
			P.append([prevEnd, currStart])
	
	# Print the intervals 
	for i in P:
		print(i)
	
# Driver code 
if __name__ == "__main__":
	
	# Given List of intervals 
	arr = [ [ 1, 3 ], [ 2, 4 ],
			[ 3, 5 ], [ 7, 9 ] ]
	
	N = len(arr)
	
	# Function call
	findFreeinterval(arr, N)
