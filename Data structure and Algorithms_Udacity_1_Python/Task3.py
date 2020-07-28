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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def get_area_codes():
	area_codes=set()
	number_of_total_call=0
	number_of_fixed_line_calls=0
	for row in calls:
		if "(080)" in row[0]:
			number_of_total_call=number_of_total_call+1
			if "(0" in row[1]:
				area_codes.add(row[1][0:row[1].find(")")+1])
				if row[1].startswith('(080)'):
					number_of_fixed_line_calls = number_of_fixed_line_calls +1
			elif row[1].startswith('140'):
				area_codes.add('140')
			elif row[1].startswith('7') or row[1].startswith('8') or row[1].startswith('9'):
				area_codes.add(row[1][0:4])
	print("The numbers called by people in Bangalore have codes: \n"+"\n".join(sorted(area_codes)))
	print(str("{:.2f}".format(float(number_of_fixed_line_calls*100/number_of_total_call)))+" percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
	
	
get_area_codes()