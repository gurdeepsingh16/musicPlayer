import re

s = 'GeeksforGeeks: A computer science  for geeks'

match = re.search(r'portal', s)

if match is None:
    print(False)
else:
    print('Start Index:', match.start())
    print('End Index:', match.end())
