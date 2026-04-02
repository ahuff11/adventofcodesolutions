import csv
from typing import List

def read () ->List[tuple]:
    file_path = "Day 2/input.csv"
    output = []
    try:
        with open(file_path, 'r',) as file:
            reader = csv.reader(file)
          
            for row in reader:    
                for i in row:     
                    getfirstandlast = i.split("-") 
                    output.append((getfirstandlast[0], getfirstandlast[1]))
                
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    return output

def findBadIDs(l : List[tuple]) -> int:
    badids = 0
    for firstID, lastID in l:
        firstlen, lastlen = len(firstID), len(lastID)
        firstIDNum, lastIDNum = int(firstID), int(lastID)
        
        if isGoodIDS(firstlen) and isGoodIDS(lastlen):
            low, high = int(getHalfofString(firstID)), int(getHalfofString(lastID))    
            magnitude = 10 ** (firstlen //2)
            for i in range(low, high +1):
                candidate = i *magnitude +i 
                if firstIDNum <= candidate <= lastIDNum:
                    badids+=candidate

        elif isGoodIDS(firstlen) and isGoodIDS(lastlen) == False:
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
