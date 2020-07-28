# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
	def __init__(self, value=""):
		# Initialize the node with children as before, plus a handler
		self.value = value
		self.next = {}
		self.handler = None
	def insert(self,  next_path, handler=None):
		# Insert the node as before
		self.next[next_path] = self.next.get(next_path, RouteTrieNode(next_path))
		self.next[next_path].handler = handler

class RouteTrie:
	def __init__(self):
		# Initialize the trie with an root node and a handler, this is the root path or home page node
		self.next = {}
		self.handler = None
		self.root='/'
	def insert(self, path, hand):
		# Similar to our previous example you will want to recursively add nodes
		# Make sure you assign the handler to only the leaf (deepest) node of this path
		curr = self.next
		sub_paths = path.split('/')
		for sub in sub_paths:
			curr.insert(RouteTrieNode(sub))
			curr = curr.next[sub]
		curr.handler = hand
	def find(self, path):
		# Starting at the root, navigate the Trie to find a match for this path
		# Return the handler for a match, or None for no match
		if path == '/':
			return self.handler
		sub_paths = path.split('/')
		curr = self.root
		for sub_path in path:
			curr = curr.next
			curr = curr[sub_path]
		handler = curr.handler
# The Router class will wrap the Trie and handle 
class Router:
	def __init__(self, root_hand, not_found):
		# Create a new RouteTrie for holding our routes
		# You could also add a handler for 404 page not found responses as well!
		self.handler = root_hand
		self.next = {}
		self.not_found = not_found
	def lookup(self, path):
		# lookup path (by parts) and return the associated handler
		# you can return None if it's not found or
		# return the "not found" handler if you added one
		# bonus points if a path works with and without a trailing slash
		# e.g. /about and /about/ both return the /about handler
		if path == '/':
			return self.handler
		sub_paths = self.split_path(path)
		curr = self
		for sub_path in sub_paths:
			if sub_path:
				if sub_path in curr.next:
					curr = curr.next
					curr = curr[sub_path]
				else:
					return self.not_found
		handler = curr.handler
		if handler:
			return handler
		else:
			return None
	def add_handler(self, path, path_handler):
		# Add a handler for a path
		# You will need to split the path and pass the pass parts
		# as a list to the RouteTrie
		if path == '/':
			self.handler = path_handler
		else:
			sub_paths = self.split_path(path)
			curr = self.next
			x = 1
			for sub_path in sub_paths:
				if not sub_path:
					continue
				if x:
					x = 0
					curr[sub_path] = curr.get(sub_path, RouteTrieNode(sub_path))
					curr = curr[sub_path]
				else:
					curr.insert(sub_path, path_handler)

	def split_path(self, path):
		# you need to split the path into parts for 
		# both the add_handler and loopup functions,
		# so it should be placed in a function here
		return path.split('/')

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one