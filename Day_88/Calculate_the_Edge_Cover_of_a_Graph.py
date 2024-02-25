
import math
def edgeCover(n):
	
	result = 0
	
	result = math.ceil(n / 2.0)
	
	return result
		
# Driver code	 
if __name__ == "__main__" : 
	n = 5
	print(int(edgeCover(n)))
