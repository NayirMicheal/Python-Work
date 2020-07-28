class Group(object):
	def __init__(self, _name):
		self.name = _name
		self.groups = []
		self.users = []

	def add_group(self, group):
		self.groups.append(group)

	def add_user(self, user):
		self.users.append(user)

	def get_groups(self):
		return self.groups

	def get_users(self):
		return self.users

	def get_name(self):
		return self.name

def is_user_in_group(user, group):
	"""
	Return True if user is in the group, False otherwise.

	Args:
		user(str): user name/id
		group(class:Group): group to check user membership against
	"""
	result=False
	users = group.get_users()
	if user in users:
		return True
	else:
		Groups=group.get_groups()
		for Group in Groups:
			result = is_user_in_group(user, Group)
			if result:
				break
		return result

#test case1
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group(sub_child_user,sub_child))
print(is_user_in_group(sub_child_user,child))
print(is_user_in_group(sub_child_user,parent))
print("\n\n")
#test case 2
G1 = Group("group1")
G2 = Group("group2")
sub_G1 = Group("sub_group1")

sub_G1_user = "sub_group1_user"
sub_G1.add_user(sub_child_user)

G1.add_group(sub_G1)

print(is_user_in_group(sub_child_user,G1))
print(is_user_in_group(sub_child_user,G2))
print(is_user_in_group(sub_child_user,sub_G1))
print("\n\n")
#test case 3
superG = Group("Supergroup")
G1 = Group("group1")
G2 = Group("group2")
sub_G1 = Group("sub_group1")
sub_G2 = Group("sub_group2")

sub_G1_user = "sub_group1_user"
sub_G1.add_user(sub_G1_user)

sub_G2_user = "sub_group2_user"
sub_G2.add_user(sub_G2_user)

G1.add_group(sub_G1)
G2.add_group(sub_G2)
superG.add_group(G1)
superG.add_group(G2)

print(is_user_in_group(sub_G1_user,G1))
print(is_user_in_group(sub_G1_user,G2))
print(is_user_in_group(sub_G1_user,sub_G1))
print(is_user_in_group(sub_G1_user,sub_G2))
print(is_user_in_group(sub_G1_user,superG))
print("\n\n")
print(is_user_in_group(sub_G2_user,G1))
print(is_user_in_group(sub_G2_user,G2))
print(is_user_in_group(sub_G2_user,sub_G1))
print(is_user_in_group(sub_G2_user,sub_G2))
print(is_user_in_group(sub_G2_user,superG))
print("\n\n")
