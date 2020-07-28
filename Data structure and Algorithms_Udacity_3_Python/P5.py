## Represents a single node in the Trie
class TrieNode:
	def __init__(self):
		## Initialize this node in the Trie
		self.is_word = False
		self.children = {}
	
	def insert(self, char):
		## Add a child node in this Trie
		self.children[char] = TrieNode()
	def suffixes(self, suffix = ''):
		## Recursive function that collects the suffix for 
		## all complete words below this point
		if self.children:
			for c, current_node in self.children.items():
				if current_node.is_word:
					suff.append(suffix + c)
				current_node.suffixes(suffix + c)
		return suff       
## The Trie itself containing the root node and insert/find functions
class Trie:
	def __init__(self):
		## Initialize this Trie (add a root node)
		self.root = TrieNode()

	def insert(self, word):
		## Add a word to the Trie
		current_node = self.root
		for char in word:
			if not char in current_node.children:
				current_node.insert(char)
			current_node = current_node.children[char]
		current_node.is_word = True

	def find(self, prefix):
		## Find the Trie node that represents this prefix
		current_node = self.root
		for w in prefix:
			if w in current_node.children:
				current_node =current_node.children[w]
			else:
				return None
		return current_node
		
MyTrie = Trie()
wordList = [
	"ant", "anthology", "antagonist", "antonym", #case 1
	"fun", "function", "factory", #case 2
	"trie", "trigger", "trigonometry", "tripod" #case 3
]
for word in wordList:
	MyTrie.insert(word)
suff=list()
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
	if prefix != '':
		prefixNode = MyTrie.find(prefix)
		if prefixNode:
			print('\n'.join(prefixNode.suffixes()))
			suff.clear()# kindly add this line in the code when testing it will clear the previous results and make the suffixes updated
		else:
			print(prefix + " not found")
	else:
		print('')
interact(f,prefix='');