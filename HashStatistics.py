#HashStatistics.py for HW 4 -2 Hash Something Out
#The functions for measuring and outputting the statistics
#Originally was intending separate files for hash functions so made this a different doc
#kept to stop clutter in HashItOutMaker.py

#Thomas Frisk
#Last Edited 4/20/26

import time

#HashStatistics is how we measure and output statistics
class HashStatistics:
    def __init__(self):
        self.collisions = 0 #how many times multiple items are appended to an index
                            #will be iterated on in HashItOutMaker
        self.start = 0 #start time
        self.end = 0 #end time

    #defines start time
    def startTime(self):
        self.start = time.time()

    #defines end time
    def endTime(self):
        self.end = time.time()

    #after startTime and endTime are calculated, calculates and returns the difference
    def hashTime(self):
        return self.end - self.start
    
    def totalBuckets(self, hashTable):
        return len(hashTable)
    
    #blanKSpaceByTaylorSwift
    #parameter:
        #hashtable, the predefined hash table size we made for function
    #returns: iterates through hashtable to see which indeces are empty/wasted
    def blankSpaceByTaylorSwift(self, hashTable):
        blankSpace = 0
        for bucket in hashTable:
            if bucket is None:
                blankSpace += 1
        return blankSpace
    
    #takes in completed hashTable and outputs required efficiency stats
    def printStats(self, hashTable):
        print("Total Buckets:", self.totalBuckets(hashTable)) #added this when
        #I realized I'm going to be making smaller buckets in later iterations
        print("Wasted Buckets:", self.blankSpaceByTaylorSwift(hashTable))
        print("Collisions:", self.collisions)
        print("Table time:", self.hashTime())