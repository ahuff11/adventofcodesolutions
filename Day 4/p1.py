import collections


def readInput() -> list[list[str]]:
    file = "Day 4/input.txt"
    matrix = []

    try:
        with open(file, 'r') as file:
            for line in file:  
                matrix.append(list(line.strip()))


        return matrix
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
        return 0
    

def findRolls(matrix : list[list[str]]) -> int:
    count = 0
    q = collections.deque()
    ROWS, COLS = len(matrix), len(matrix[0])
    neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

   # print(matrix[1][1])
    for r in range(ROWS):
        for c in range(COLS):

            if matrix[r][c] == "@":
                county = 0
                for dr, dc in neighbors:
                    nr, nc = dr+r, dc+ c
                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or matrix[nr][nc] == ".":
                        continue
                    county +=1 
                if county <=3:
                    count+=1
    
    return count





def main():

    input = readInput()
    # for i in input:
    #     print(i)
    
    print(findRolls(input))

if __name__ == "__main__":
    main()
