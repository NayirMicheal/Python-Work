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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
def get_possible_telemarkets():
    telemarketers = set()
    outgoing_calls = set([row[0] for row in calls])
    received_calls = set([row[1] for row in calls])
    send_txt = set([row[0] for row in texts])
    receive_txt = set([row[1] for row in texts])
    telemarketers = outgoing_calls - received_calls - send_txt - receive_txt
    print("These numbers could be telemarketers: \n"+"\n".join(sorted(telemarketers)))
	
get_possible_telemarkets()