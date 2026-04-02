import csv
from typing import List
# store them as pairs in a list (123, 123)
# since its only pairs odd length johnsons wont work
# we can get the length divide by two to get our split
# we can check if length invalid check the length of 2nd number
# how can we round up our new minimum if the 
# we can use the ord 
def read () ->List[tuple]:
    file_path = "Day 2/input.csv"
    output = []
    try:
        with open(file_path, 'r',) as file:
            reader = csv.reader(file)
            # iterates once and returns the whole line seperated into a list
            for row in reader:    #O(1)
                for i in row:     #O(n)
                    getfirstandlast = i.split("-") #O(n)
                    output.append((getfirstandlast[0], getfirstandlast[1]))
                
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    return output
#44487518055
#assuming all ranges
def findBadIDs(l : List[tuple]) -> int:
    badids = 0
    for firstID, lastID in l:
        firstlen, lastlen = len(firstID), len(lastID)
        firstIDNum, lastIDNum = int(firstID), int(lastID)
        
       
        # if not isGoodIDS(firstlen) and not isGoodIDS(lastlen):
        #     continue
        
        # if isGoodIDS(firstlen) and not isGoodIDS(lastlen):
        #     lastlen -=1 
        #     lastIDNum = (10 ** lastlen) -1
            

        # if not isGoodIDS(firstlen) and isGoodIDS(lastlen):
        #     firstlen +=1
        #     firstIDNum = 10**(firstlen)
            
        
        # magnitude = 10 ** (firstlen //2)
        # low = firstIDNum //magnitude
        # high = lastIDNum//magnitude

        # for i in range(low, high +1):
        #     candidate = i *magnitude +i 
        #     if firstIDNum <= candidate <= lastIDNum:
        #         badids+=candidate

        if isGoodIDS(firstlen) and isGoodIDS(lastlen):
            low, high = int(getHalfofString(firstID)), int(getHalfofString(lastID))    
            magnitude = 10 ** (firstlen //2)
            for i in range(low, high +1):
                candidate = i *magnitude +i 
                if firstIDNum <= candidate <= lastIDNum:
                    badids+=candidate

        elif isGoodIDS(firstlen) and isGoodIDS(lastlen) == False:
            #set digit size equal to the first length
            lastlen = firstlen
            lastID = str((10 ** lastlen) -1)
            magnitude = 10 ** (firstlen //2)
            low, high = int(getHalfofString(firstID)), int(getHalfofString(lastID))            
            for i in range(low, high +1):
                candidate = i *magnitude +i 
                if firstIDNum <= candidate <= lastIDNum:
                    badids+=candidate
            
        elif isGoodIDS(firstlen) == False and isGoodIDS(lastlen):
            firstlen = lastlen
            firstID = str(10**(firstlen))
            magnitude = 10 ** (firstlen //2)
            low, high = int(getHalfofString(firstID)), int(getHalfofString(lastID))           
            for i in range(low, high +1):
                candidate = i *magnitude +i 
                if firstIDNum <= candidate <= lastIDNum:
                    badids+=candidate
        else:
            #both are odd and cannot contain valid sequence
            continue
        
    return badids


def getHalfofString(s : str) -> str:
    mid = len(s)//2
    newstring = s[:mid]
    return newstring

def isGoodIDS(length :int) ->bool:
    if length % 2 == 0:
        return True
    else:
        return False


def main():
    ide = read()
    print(findBadIDs(ide))
    

if __name__ == "__main__":
    main()
    #is there a mathmatical formula or like theory of finding number sequences that are repeated twice in a range of numbers?