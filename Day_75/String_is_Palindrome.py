stack = []
top = -1

# push function
def push(ele: str):
	global top
	top += 1
	stack[top] = ele

# pop function
def pop():
	global top
	ele = stack[top]
	top -= 1
	return ele

def isPalindrome(string: str) -> bool:
	global stack
	length = len(string)

	# Allocating the memory for the stack
	stack = ['0'] * (length + 1)

	# Finding the mid
	mid = length // 2
	i = 0
	while i < mid:
		push(string[i])
		i += 1

	if length % 2 != 0:
		i += 1
	while i < length:
		ele = pop()

		if ele != string[i]:
			return False
		i += 1
	return True
if __name__ == "__main__":

	string = "madam"

	if isPalindrome(string):
		print("Yes")
	else:
		print("No")

