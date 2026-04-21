#HashItOutMaker.py for the second HW4: Hash Something Out
#Purpose: This file is taking in the DataReader and HashStatistics file to make and measure
#the efficacy of the hash table.

#Thomas Frisk
#Last Edited 4/20/26
#Sorry for the late. Been crazy couple of weeks.

#Iteration 5: the bad Linear Probing Table

from HashStatistics import HashStatistics
from DataReader import loadData


data = loadData("MOCK_DATA.csv")

# in the HashStatistics File. this just will display the required stats
curStats = HashStatistics()



#Defining the initial hash table sizes for title hash and quote hash tables
titleHashTable = [None] * 15000
quoteHashTable = [None] * 15000



#This class defines the Node for the linear probe method
    #key (movie title or quote we will hash)
    #record: MovieRecord from Datareader
class Node:
    def __init__(self, key, record):
        self.key = key
        #We are going to have a list of all the record items from the reader
        self.records = [record]
        #self.next = None #commenting out for Linear Probing

#iteration 06, bad hash 
#the same bad hash as linkedlist1:
def badHashFunction(key, tableSize):
    return len(key) % tableSize


#I then modulus by len(hashtable) to ensure it's in range
def linearProbeHash(hashTable, key, record, stats):
    index = badHashFunction(key, len(hashTable))

    # if empty, insert immediately
    if hashTable[index] is None:
        hashTable[index] = Node(key, record)
        return

    # otherwise probe forward
    while hashTable[index] is not None:
        stats.collisions += 1

        if hashTable[index].key == key:
            hashTable[index].records.append(record)
            return

        index = (index + 1) % len(hashTable)

    hashTable[index] = Node(key, record)

# This function inserts a record into the hash table using linked list chaining
# Parameters:
#   hashTable: the table being built
#   key: the movie title or quote used as the key
#   record: the MovieRecord object from DataReader
# def linkedListHash(hashTable, key, record):
#     index = finalListHashFunction(key, len(hashTable))

#     if hashTable[index] is None:
#         hashTable[index] = Node(key, record)
#         return

#     current = hashTable[index]

#     #collision adder
#     while current is not None:
#         curStats.collisions += 1

#         if current.key == key:
#             current.records.append(record)
#             return

#         if current.next is None:
#             current.next = Node(key, record)
#             return

#         current = current.next








#Using linkedlist for title and quote

print("iteration 05: bad linear probe")
#title as key
print("Title as Key")
curStats.startTime()

for record in data:
    if record.movie_title != "":
        linearProbeHash(titleHashTable, record.movie_title, record, curStats)

curStats.endTime()

curStats.printStats(titleHashTable)

#quote as key
print("Quote as Key")
curStats = HashStatistics()
curStats.startTime()

for record in data:
    if record.quote != "":
        linearProbeHash(quoteHashTable, record.quote, record, curStats)

curStats.endTime()

curStats.printStats(quoteHashTable)