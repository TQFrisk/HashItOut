#HashItOutMaker.py for the second HW4: Hash Something Out
#Purpose: This file is taking in the DataReader and HashStatistics file to make and measure
#the efficacy of the hash table.

#Thomas Frisk
#Last Edited 4/20/26
#Sorry for the late. Been crazy couple of weeks.

#Iteration 4: the even final linked list hash table 

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


#this is the final linked list iteration
#For this one I thought of starting with more variation by starting with multiplying the
#index by the order of key for each one. it wasn't great at first so I started by adding
#1, and I got a better result, then I tried +2 and got better, then +3 and got even better
#then +4 got worse so I stuck to 3

#I then modulus by tablesize to ensure it's in range
def finalListHashFunction(key, tableSize):

    if key == "":
        return 0

    sumOfChars = 0
    for i in range(len(key)):
        sumOfChars += (i+3) * ord(key[i])

    return sumOfChars % tableSize

# This function inserts a record into the hash table using linked list chaining
# Parameters:
#   hashTable: the table being built
#   key: the movie title or quote used as the key
#   record: the MovieRecord object from DataReader
def linkedListHash(hashTable, key, record):
    index = finalListHashFunction(key, len(hashTable))

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

print("iteration 04: Final linked list")
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