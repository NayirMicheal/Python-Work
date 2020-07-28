import hashlib
import datetime  
import time

def get_time_gmt_now():
	return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d T %H:%M:%S.%f%Z")
	
def calc_hash(data):
	sha = hashlib.sha256()
	hash_str = data.encode('utf-8')
	sha.update(hash_str)
	return sha.hexdigest()
	
class Block:
	def __init__(self, data,previous_hash=0):
		self.timestamp = get_time_gmt_now()
		self.data = data
		self.previous_hash = previous_hash
		self.hash = calc_hash(self.data)
		self.next = None
	def get_hash(self):
		return self.hash
	def get_previous_hash(self):
		return self.previous_hash
	def set_next_block(self):
		self.next=next
		return
	def get_next_block(self):
		return self.next 
	def __str__(self):
		return "\nTime Stamp: "+str(self.timestamp)+"\n"+"Data: "+str(self.data)+"\n"+"Previous Hash: "+str(self.previous_hash)+"\n"+"Hash: "+str(self.hash) + "\n"

class BlockChain:
	def __init__(self,block=None):
		self.head = block
		self.tail = block
	def add_block(self,data):
		new_block = self.head
		if new_block is None:
			self.head=Block(data)
			self.tail = self.head
		else:
			block=Block(data,self.tail.get_hash())
			self.tail.next = block
			self.tail = block
		return
			
		return
	def size(self):
		block = self.head
		size =0	
		while block:
			size +=1
			block = block.next
		return size
	def print_Block_chain(self):
	#return a list of blocks
		block = self.head
		while block:
			print(block)
			block = block.next
		return
#test case1  
print("############TEST CASE1###############")
B1 = Block("Hello")
BC = BlockChain(B1)
time.sleep(2)
BC.add_block("My name")
time.sleep(1)
BC.add_block("Is")
BC.add_block("######")
BC.add_block("I")
BC.add_block("am")
BC.add_block("From")
BC.add_block("******")
BC.print_Block_chain()


#test case 2
print("############TEST CASE2###############")
BC2 = BlockChain()
print("size",BC2.size())
BC2.print_Block_chain()


#test case 3 
print("############TEST CASE3###############")
BC3 = BlockChain()
print("size",BC3.size())
BC3.add_block("Hello From")
print("size",BC3.size())
BC3.add_block("the other")
print("size",BC3.size())
BC3.add_block("side")
print("size",BC3.size())
BC3.print_Block_chain()