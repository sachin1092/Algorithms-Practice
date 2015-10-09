import random

class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node

def Insert(head, data):
    node = Node()
    node.data = data
    node.next = None
    if head == None:
        head = node
    else:
    	temp = head
    	while temp.next != None:
        	temp = temp.next
    	temp.next = node
    return head

def Insert_At_Head(head, data):
	node = Node()
	node.data = data
	node.next = None
	if head is not None:
		node.next = head
	head = node
	return head

def InsertNth(head, data, position):
	node = Node()
	node.next = None
	node.data = data
	if head == None:
		return node
	elif position == 0:
		node.next = head
		return node
	else:
		temp = head
		for __ in xrange(1, position):
			if temp.next == None:
				temp.next = node
				return head
			temp = temp.next

		temp2 = temp.next
		temp.next = node
		node.next = temp2
		return head

def Delete(head, position):
	if head == None:
		return head
	elif position == 0:
		node = head.next
		head = node
		return head
	else:
		temp = head
		for __ in xrange(1, position):
			temp = temp.next
		temp.next = temp.next.next
		return head


def print_list(head):
	print "List:"
	while head != None:
		print head.data, "=>",
		head = head.next
	print "None\n"

if __name__ == "__main__":
	node = None
	for i in xrange(10):
		val = input("Enter Value: ")
		pos = random.randint(0, i)
		node = InsertNth(node, val, pos)
	print_list(node)
	delPos = input("Enter position to delete node:")
	while delPos != -1:
		node = Delete(node, delPos)
		print_list(node)
		delPos = input("Enter position to delete node:")