"""
Authors: Vatche, Zack Wei, Dash
"""


from short import getShortStr


words = []

for i in range(5):
    word = input("Enter a word: ")
    words.append(word)

shortest_word = getShortStr(words)

file = open("shortest.txt","w")
file.write(shortest_word)
file.close()



