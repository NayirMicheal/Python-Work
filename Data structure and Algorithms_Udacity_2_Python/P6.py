class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
	def __str__(self):
		cur_head = self.head
		out_string = ""
		if cur_head:
			while cur_head:
				out_string += str(cur_head.value) + " -> "
				cur_head = cur_head.next
			return out_string[:-4]
		else:
			out_string = "Empty LinkedList"
			return out_string


	def append(self, value):
		if self.head is None:
			self.head = Node(value)
			self.tail = self.head
			return
		else:
			node = Node(value)
			self.tail.next = node
			self.tail = node

	def size(self):
		size = 0
		node = self.head
		while node:
			size += 1
			node = node.next

		return size
	def from_list_or_set_to_linkedList(self,set_list):
		for elem in set_list:
			self.append(elem)

def union(llist_1, llist_2):
    # Your Solution Here
	union_set = set()
	sol = LinkedList()
	head1=llist_1.head
	head2=llist_2.head
	while head1:
		union_set.add(head1.value)
		head1 = head1.next
	while head2:
		union_set.add(head2.value)
		head2 = head2.next
	sol.from_list_or_set_to_linkedList(union_set)
	return sol
	pass

def intersection(llist_1, llist_2):
    # Your Solution Here
	dic = {}
	intersection_list = []
	sol = LinkedList()
	head1=llist_1.head
	head2=llist_2.head
	union_set1 = set()
	union_set2 = set()
	while head1:
		union_set1.add(head1.value)
		head1 = head1.next
	while head2:
		union_set2.add(head2.value)
		head2 = head2.next
	for elem in union_set1:
		dic[elem]=1
	for elem in union_set2:
		if elem in dic.keys():
			dic[elem]+=1
		else:
			dic[elem] =1
	for num, freq in dic.items():
		if freq == 2:
			intersection_list.append(num)
	sol.from_list_or_set_to_linkedList(intersection_list)
	return sol
	pass


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1] 

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ("Union : "+str(union(linked_list_1,linked_list_2))) #3,2,4,35,6,65,21,32,9,1,11
print ("Intersection : "+str(intersection(linked_list_1,linked_list_2)))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ("Union : "+str(union(linked_list_3,linked_list_4)))
print ("Intersection : "+str(intersection(linked_list_3,linked_list_4)))

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3,2,4,35,55,6,11,5,6,4,3,23,96]
element_2 = [1,7,8,9,11,55,21,1,22,74,3,1,5]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print ("Union : "+str(union(linked_list_5,linked_list_6)))
print ("Intersection : "+str(intersection(linked_list_5,linked_list_6)))
