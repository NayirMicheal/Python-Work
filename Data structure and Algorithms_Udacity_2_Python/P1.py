from collections import OrderedDict
class LRU_Cache(object):

	def __init__(self, capacity=5):
		# Initialize class variables
		self.cache=OrderedDict()
		self.cap=capacity
		for i in range(capacity+1):
			self.cache[i]=None
		pass

	def get(self, key):
		# Retrieve item from provided key. Return -1 if nonexistent.
		if key in self.cache.keys():
			self.cache.move_to_end(key)
			return self.cache[key]
		else:
			return -1
		pass

	def set(self, key, value):
		# Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
		self.cache[key]=value
		self.cache.move_to_end(key)
		if len(self.cache) > self.cap:
			self.cache.popitem(False)
		pass

#test case 1
print("########TEST CASE 1###########")
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

#test case 2
print("########TEST CASE 2###########")
our_cache2 = LRU_Cache(7)

our_cache2.set(1, 1);
our_cache2.set(2, 3);
our_cache2.set(3, 5);
our_cache2.set(4, 7);
our_cache2.set(5, 9);

#still two places empty
our_cache2.set(6, 11) 
our_cache2.set(7, 13)
#it is full now


print(our_cache2.get(7))     # returns 13
our_cache2.set(7, 20)
print(our_cache2.get(7))     # returns 20

our_cache2.set(8, 110);

print(our_cache2.get(1))       # returns -1 as least used
print(our_cache2.get(2))       # returns 3
print(our_cache2.get(3))      # returns 5
print(our_cache2.get(4))     # returns 9
print(our_cache2.get(5))     # returns 11
print(our_cache2.get(6))     # returns 11
print(our_cache2.get(7))     # returns 20
print(our_cache2.get(8))     # returns 110


#test case 2
print("########TEST CASE 3###########")
our_cache3 = LRU_Cache(7)

our_cache3.set(1, 1);
print(our_cache3.get(1))       # returns 1
print(our_cache3.get(2))       # returns None
print(our_cache3.get(3))      # returns None
print(our_cache3.get(4))     # returns None
print(our_cache3.get(5))     # returns None
print(our_cache3.get(6))     # returns None
print(our_cache3.get(7))     # returns None
print(our_cache3.get(8))     # returns -1
