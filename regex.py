import re

message = 'Hello World!'
pattern  = r'world'
result = re.search(pattern, message, flags=re.IGNORECASE)
if result: 
    print('Pattern found')

else:
    print('Pattern not found')
