
class Node:

	def __init__(self, x):

		self.data = x
		self.next = None

def printList(node):

	while (node != None):
		print(node.data,
			end=" ")
		node = node.next

def mergeKLists(arr, last):

	for i in range(1, last + 1):
		while (True):
	
			head_0 = arr[0]
			head_i = arr[i]

			# Break if list ended
			if (head_i == None):
				break
			if (head_0.data >=
					head_i.data):
				arr[i] = head_i.next
				head_i.next = head_0
				arr[0] = head_i
			else:
				# Traverse the first list
				while (head_0.next != None):

					if (head_0.next.data >=
							head_i.data):
						arr[i] = head_i.next
						head_i.next = head_0.next
						head_0.next = head_i
						break
					# go to next node
					head_0 = head_0.next
					# if last node
					if (head_0.next == None):
						arr[i] = head_i.next
						head_i.next = None
						head_0.next = head_i
						head_0.next.next = None
						break
	return arr[0]


# Driver code
if __name__ == '__main__':

	# Number of linked
	# lists
	k = 3

	# Number of elements
	# in each list
	n = 4

	arr = [None for i in range(k)]

	arr[0] = Node(1)
	arr[0].next = Node(3)
	arr[0].next.next = Node(5)
	arr[0].next.next.next = Node(7)

	arr[1] = Node(2)
	arr[1].next = Node(4)
	arr[1].next.next = Node(6)
	arr[1].next.next.next = Node(8)

	arr[2] = Node(0)
	arr[2].next = Node(9)
	arr[2].next.next = Node(10)
	arr[2].next.next.next = Node(11)

	# Merge all lists
	head = mergeKLists(arr, k - 1)

	printList(head)
