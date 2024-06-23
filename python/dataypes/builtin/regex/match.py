import re

text = "There is a table in the room"
pattern = r'table'

match = re.match(pattern, text)

if match:
    print('The match found', match.group())
else:
    print('Match not foumd')
