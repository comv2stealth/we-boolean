f1 = open("log.txt", "r")
list1 = []
for line in f1:
   list1.append(line)

import string
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = list1.count(letter) + list1.count(letter.upper())

def split(word): 
    return [char for char in word]

def getProbability(word):
    wordList = split(word)
    ansList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    charList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for n in range(len(charList)):
        ansList[n] = (wordList.count(charList[n]))/len(word)
    return ansList

def dot(K, L):
   if len(K) != len(L):
      return 0
   return sum(i[0] * i[1] for i in zip(K, L))


f = open("dictionary.txt", "r")
for n in values:
    val = values[n]
    values[n] = float(val/len(list1))
    print(values[n])
words = dict()

dictmap = dict()

for x in f:
    listx = getProbability(x)
    val = dot(listx, values[x])
    dictmap[x] = val



print(max(dictmap, key = dictmap.get))
