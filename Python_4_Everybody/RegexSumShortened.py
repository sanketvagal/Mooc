import re

print sum(int(i) for i in (re.findall('[0-9]+', open('sumregex.txt').read())))
