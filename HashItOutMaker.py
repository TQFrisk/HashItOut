#HashItOutMaker.py for the second HW4: Hash Something Out
#Purpose: This file is taking in the DataReader and HashStatistics file to make and measure
#the efficacy of the hash table.

#Thomas Frisk
#Last Edited 4/20/26
#Sorry for the late. Been crazy couple of weeks.

#Iteration 2: the Better table - see academic honesty note below

from HashStatistics import HashStatistics
from DataReader import loadData


data = loadData("MOCK_DATA.csv")

# in the HashStatistics File. this just will display the required stats
curStats = HashStatistics()



#Defining the initial hash table sizes for title hash and quote hash tables
#They are the size of qty rows in this iteration to be the inefficient method
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


#this is the first iteration of the hash function made intentionally bad
#it takes the string for the key (movie or quote) and hashes into bucket index
#in this case it's the length of the string % length of table to ensure it's within table bounds
def betterHashFunction(key, tableSize):
    """Academic Honesty: So i was sick the day you went over this in class 
    and this is the general method I saw on todo. I'm doing another improvement that required because
    I found this method online, but I wanted honesty in how I know https://www.w3schools.com/python/python_dsa_hashtables.asp """
    sumOfChars = 0
    for char in key:
        sumOfChars += ord(char)
    return sumOfChars % tableSize

# This function inserts a record into the hash table using linked list chaining
# Parameters:
#   hashTable: the table being built
#   key: the movie title or quote used as the key
#   record: the MovieRecord object from DataReader
def linkedListHash(hashTable, key, record):
    index = betterHashFunction(key, len(hashTable))

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




#Using iteration 1 for title and quote

print("Better linked list: sum ord(char)")
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