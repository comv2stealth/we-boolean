list1 = []
import string
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
    values[letter] = index + 27;
for n in values:
    print(n)
    
