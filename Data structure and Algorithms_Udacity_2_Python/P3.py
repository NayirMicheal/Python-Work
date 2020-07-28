import sys
from collections import  defaultdict
import heapq
			
#reference https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/		
def get_frequency (data):
	all_freq = {} 
	for i in data: 
		if i in all_freq: 
			all_freq[i] += 1
		else: 
			all_freq[i] = 1
	return all_freq
	
def Huffman_encoded_data(huff,data):
	encode_str=[]
	for str in data:
		for list in huff:
			if str in list:
				encode_str.append(list[1])
	encoded_data = ''.join(encode_str)
	return encoded_data
	
def huffman_encoding(data):
	if len(data) == 0:
		return "",[]
	frequency = defaultdict(int)
	frequency = get_frequency(data)	
	huff = encode(frequency)
	encoded_data = Huffman_encoded_data(huff,data)
	return encoded_data ,huff
 

def encode(frequency):
	heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
	heapq.heapify(heap)
	while len(heap) > 1:
		lo = heapq.heappop(heap)
		hi = heapq.heappop(heap)
		for pair in lo[1:]:
			pair[1] = '0' + pair[1]
		for pair in hi[1:]:
			pair[1] = '1' + pair[1]
		heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
	return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
	pass
def convert(lst): 
	items = {}
	for item in lst:
		key, value = item[1],item[0]
		items[key] = value
	return items
def huffman_decoding(data,codes):
	dict = convert(codes)#contains code for each object
	res = ""
	while data:
		for k in dict:
			if data.startswith(k):
				res += dict[k]
				data = data[len(k):]
	return res

if __name__ == "__main__":
	codes = {}
	print("########### TEST CASE 1###########")
	a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"

	print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
	print ("The content of the data is: {}\n".format(a_great_sentence))
	encoded_data,codes=huffman_encoding(a_great_sentence)
	# encoded_data, tree = huffman_encoding(a_great_sentence)
	
	print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
	print ("The content of the encoded data is: {}\n".format(encoded_data))

	decoded_data = huffman_decoding(encoded_data,codes)

	print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
	print ("The content of the encoded data is: {}\n".format(decoded_data))
	
	print("########### TEST CASE 2###########")
	a_great_sentence = "The bird is the word"

	print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
	print ("The content of the data is: {}\n".format(a_great_sentence))
	encoded_data,codes=huffman_encoding(a_great_sentence)
	# encoded_data, tree = huffman_encoding(a_great_sentence)
	
	print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
	print ("The content of the encoded data is: {}\n".format(encoded_data))

	decoded_data = huffman_decoding(encoded_data,codes)

	print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
	print ("The content of the encoded data is: {}\n".format(decoded_data))
	
	print("########### TEST CASE 3###########")
	a_great_sentence = ""

	print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
	print ("The content of the data is: {}\n".format(a_great_sentence))
	encoded_data,codes=huffman_encoding(a_great_sentence)
	if len(encoded_data):
		print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
		print ("The content of the encoded data is: {}\n".format(encoded_data))
		decoded_data = huffman_decoding(encoded_data,codes)
		print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
		print ("The content of the encoded data is: {}\n".format(decoded_data))
	else:
		print("No data to encode")