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


# Brainstorm slop
# okay didnt realize this is a grid problem. The eight neighbors is the area that surrounds the grid. 
# i think a solution could be a bit map.  
# i will probably have to pass through and save some sort of information then get the answer 
# we loop through and we store current, topleft, topmid, topright, left, right, bottomleft, bottommid, bottom right
#so we need to handle edge cases where we are at the top, bottom, lef or right
# if row == 0, then we dont need to worry about top
# if row == len(matrix)-1 then we don't need to worry about the bottom
# if col == 0 we don't need to worry about left, 
# if col == len(row)-1 we don't need to worry about right