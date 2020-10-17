def split(word): 
    return [char for char in word]

def getProbability(word):
    wordList = split(word)
    ansList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    charList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for n in charList:
        ansList[n] = (wordList.count(charList[n]))/len(word)
    return ansList
list1 = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
import string
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = list1.count(letter) + list1.count(letter.upper())
for n in values:
    val = 
    values[n] = float(/len(list1))
