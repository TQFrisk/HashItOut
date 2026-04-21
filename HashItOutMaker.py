#HashItOutMaker.py for the second HW4: Hash Something Out
#Purpose: This file is taking in the DataReader and HashStatistics file to make and measure
#the efficacy of the hash table.

#Thomas Frisk
#Last Edited 4/20/26
#Sorry for the late. Been crazy couple of weeks.

#Iteration 3: the even Better linked list table 

from HashStatistics import HashStatistics
from DataReader import loadData


data = loadData("MOCK_DATA.csv")

# in the HashStatistics File. this just will display the required stats
curStats = HashStatistics()



#Defining the initial hash table sizes for title hash and quote hash tables
titleHashTable = [None] * 15000
quoteHashTable = [None] * 15000



#This class defines the Node for the linked list method
#parameters: 
    #key (movie title or quote we will hash)
    #record: MovieRecord from Datareader
class Node:
    def __init__(self, key, record):
        self.key = key
        #We are going to have a list of all the record items from the reader
        self.records = [record]
        self.next = None


#this is the third iteration
#this uses the ord of last one but then multiplies by the key of the first value for better variance
#My idea here is to go from the midpoint for better spread
# If that sum is even  I subtract that from the midpoint of the table
#if that sum is odd I then add to the midpoint of the table
#I then modulus by tablesize to ensure it's in range
def evenBetterHashFunction(key, tableSize):

    #just to account for possibility of empty title/quote
    if key == "":
        return 0

    sumOfChars = 0
    for i in range(len(key)):
        sumOfChars += (i) * ord(key[i])

    if sumOfChars % 2 == 0:
        sumOfChars = tableSize//2 - sumOfChars

    else:
        sumOfChars = tableSize//2 + sumOfChars

    return sumOfChars % tableSize


# This function inserts a record into the hash table using linked list chaining
# Parameters:
#   hashTable: the table being built
#   key: the movie title or quote used as the key
#   record: the MovieRecord object from DataReader
def linkedListHash(hashTable, key, record):
    index = evenBetterHashFunction(key, len(hashTable))

    if hashTable[index] is None:
        hashTable[index] = Node(key, record)
        return

    current = hashTable[index]

    #collision adder
    while current is not None:
        curStats.collisions += 1

        if current.key == key:
            current.records.append(record)
            return

        if current.next is None:
            current.next = Node(key, record)
            return

        current = current.next




#Using linkedlist for title and quote

print("iteration 03: Even Better linked list")
#title as key
print("Title as Key")
curStats.startTime()

for record in data:
    linkedListHash(titleHashTable, record.movie_title, record)

curStats.endTime()

curStats.printStats(titleHashTable)

#quote as key
print("Quote as Key")
curStats = HashStatistics()
curStats.startTime()

for record in data:
    linkedListHash(titleHashTable, record.quote, record)

curStats.endTime()

curStats.printStats(titleHashTable)