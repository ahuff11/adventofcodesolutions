#inneficient solution part 1

def readranges() -> list[tuple]:
    rangeFile = "Day 5/ranges.txt"
    storedRanges = []

    try:
        with open(rangeFile, 'r') as file:
            for line in file:
                range1, range2 = line.strip().split('-', 1)
                storedRanges.append((int(range1), int(range2)))
            

            return storedRanges
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
        return 0



def readids() -> list[int]:
    idFile = "Day 5/ids.txt"
    storedIds = []
    try:
        with open(idFile, 'r') as file:
            for line in file:
                storedIds.append(int(line.strip()))

            return storedIds
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
        return 0


def main():
    ranges = readranges()
    ids = readids()
    count = 0
    for k in ids:
        for i, j in ranges:
        
            if k >= i and k <= j:
                count +=1
                break
                
    print(count)


if __name__ == "__main__":
    main()