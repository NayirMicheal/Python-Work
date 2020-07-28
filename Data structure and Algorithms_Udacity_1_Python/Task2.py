"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
def longest_call_duration():	
	tele_dict= {}
	for row in calls:
		if row[0] in tele_dict:
			tele_dict[row[0]] +=int(row[3])
			# print(tele_dict[row[0]])
		if not row[0] in tele_dict:
			tele_dict[row[0]] = int(row[3])
		if row[1] in tele_dict:
			tele_dict[row[1]] += int(row[3])
		if not row[1] in tele_dict:
			tele_dict[row[1]] = int(row[3])
	max_phone_no = max(tele_dict, key = lambda k: tele_dict[k])
	max_duration = tele_dict[max_phone_no]
	print(str(max_phone_no)+" spent the longest time, "+str(max_duration)+" seconds, on the phone during September 2016.")

longest_call_duration()


