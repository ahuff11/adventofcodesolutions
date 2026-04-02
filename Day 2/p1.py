import csv
import math
from typing import List


def read () ->List[tuple]: #O(n*L)  
    file_path = "Day 2/input.csv"
    output = []
    try:
        with open(file_path, 'r',) as file:
            reader = csv.reader(file)
            
            for row in reader:    #O(1) Only 1 row
                for i in row:     #O(n)
                    getfirstandlast = i.split("-") #O(L)
                    output.append((getfirstandlast[0], getfirstandlast[1]))
                
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    return output


def findBadIDs(l : List[tuple]) -> int:
    badids = 0
    for firstID, lastID in l: #O(n)
        firstlen, lastlen = len(firstID), len(lastID)
        firstIDNum, lastIDNum = int(firstID), int(lastID) # O(L)
        
       
        if not isGoodIDS(firstlen) and not isGoodIDS(lastlen):
            continue
        
        if isGoodIDS(firstlen) and not isGoodIDS(lastlen):
            lastlen -=1 
            lastIDNum = (10 ** lastlen) -1
            

        if not isGoodIDS(firstlen) and isGoodIDS(lastlen):
            firstIDNum = 10**(firstlen)
            firstlen +=1
            
        low_magnitude  = 10 ** (firstlen // 2)
        high_magnitude = 10 ** (lastlen // 2)  
        magnitude = low_magnitude
        while magnitude <= high_magnitude: # O(log10^(magnitude range))
                                           # O(d) where d = digit length
            low = firstIDNum //magnitude
            high = lastIDNum//magnitude
            validlow = magnitude //10

            low  = max(firstIDNum // magnitude, validlow)  
            high = math.ceil(lastIDNum  / magnitude)

            for i in range(low, high +1):  # O(n)   # O(10^(d/2))
                candidate = i *magnitude +i 
                if firstIDNum <= candidate <= lastIDNum:
                    badids+=candidate

            magnitude *= 10
        
    return badids


def isGoodIDS(length :int) ->bool:
    if length % 2 == 0:
        return True
    else:
        return False

# Time Complexity: O(n * d * 10^(d/2))
def main():
    ide = read() 
    print(findBadIDs(ide)) 
    

if __name__ == "__main__":
    main()
    