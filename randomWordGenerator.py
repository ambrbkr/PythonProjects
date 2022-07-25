#USE THIS FOR A RANDOM WORD GENERATOR

pip install random-word pyyaml

from random_word import RandomWords

random_words = RandomWords()
print(random_words.get_random_word())

#______________________________________________________________________________
#you can also create your own random word genorator
import random

#create the file
wordsstartw = open("sample.txt", "x")

#write to the file the words you want to have generate
wordsstartw.write("witch with withdrawal within without witness witnesses wives wizard wolf woman women womens won wonder wonderful wondering wood wooden woods wool worcester word wordpress words work worked worker workers workflow workforce working workout workplace works workshop workshops workstation world worlds")

#open and read the entire file
wordsstartw = open("sample.txt", "r")
print(wordsstartw.read())

#choose a random word out from the file
print(random.choice(open("sample.txt", "r").readline().split()))
