import re

str1 = "Fear leads to anger; anger leads to hatred; hatred leads to conflict"

str1 = re.sub("leads", lambda x: 'x', str1)

print(str1)

s = "Combine/Use-Not:alpha"


txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)