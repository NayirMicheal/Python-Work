"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def get_different_tele_numbers():
	different_nums = set()
	for row in texts :
		different_nums.add(row[0])
		different_nums.add(row[1])
	for row in calls :
		different_nums.add(row[0])
		different_nums.add(row[1])
	print('There are '+str(len(different_nums))+' different telephone numbers in the records.')

get_different_tele_numbers()

