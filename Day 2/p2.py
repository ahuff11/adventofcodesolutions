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
        
       
        for d in range(firstlen, lastlen+1): #O(n)
            for unit_len in range(1, d//2 +1):  
                if d % unit_len == 0:
                    magnitude = 10 ** unit_len
                    reps = d //unit_len
                    mult = (magnitude ** reps-1) //(magnitude -1)
                    low = max(math.ceil(firstIDNum/mult), 10 **(unit_len-1))
                    high = min(lastIDNum//mult, 10 **unit_len-1)
                    for i in range(low, high + 1):
                        if not isprim(str(i)):
                            continue
                        else:
                            candidate = i * mult
                            if firstIDNum <= candidate <= lastIDNum:
                                badids += candidate
    return badids


def isprim(s: str) -> bool:
    return (s + s).find(s, 1) == len(s)


# Time Complexity: O(n * d * 10^(d/2))
def main():
    ide = read() 
    print(findBadIDs(ide)) 
    

if __name__ == "__main__":
    main()
    