import collections
import time


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
    ans = 0
    q = collections.deque()
    ROWS, COLS = len(matrix), len(matrix[0])
    neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for i in range(ROWS):
        for j in range(COLS):                               # O(r*c)
            if matrix[i][j] == "@":
                q.append((i,j))



    while q:                #Memory: O(r*c)  Time: O(r*c)
        r, c = q.popleft()
        if matrix[r][c] != "@":
            continue
        count = 0
        for dr, dc in neighbors:
            nr, nc = dr+r, dc+ c
            if min(nr, nc) < 0 or nr == ROWS or nc == COLS or matrix[nr][nc] == ".":
                continue
            count +=1
        if count <= 3:
            ans +=1
            matrix[r][c] = "."
            for dr, dc in neighbors:
                nr, nc = dr+r, dc+ c
                if min(nr, nc) < 0 or nr == ROWS or nc == COLS or matrix[nr][nc] == ".":
                    continue
                q.append((nr, nc))

    return ans


#improves time by about  .01 seconds
def findRollsHash(matrix : list[list[str]]) -> int:
    ans = 0
    q = collections.deque()
    ROWS, COLS = len(matrix), len(matrix[0])
    neighbors = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    
    counts = {}  

    for i in range(ROWS):
        for j in range(COLS):                               # O(r*c)
            if matrix[i][j] != "@":
                continue
            count = 0
            for dr, dc in neighbors:
                nr, nc = i + dr, j + dc
                if min(nr, nc) < 0 or nr == ROWS or nc == COLS:
                    continue
                if matrix[nr][nc] == "@":
                    count +=1
            counts[(i,j)] = count
            if count <= 3:
                q.append((i,j))
    
    while q:
        r, c = q.popleft()
        if counts[(r, c)] > 3:       
            continue
        
        ans += 1
        matrix[r][c] = "."
            
        for dr, dc in neighbors:
            nr, nc = r + dr, c + dc
            if min(nr, nc) < 0 or nr == ROWS or nc == COLS or matrix[nr][nc] != "@":
                continue
            counts[(nr, nc)] -= 1
            if counts[(nr, nc)] == 3:   
                q.append((nr, nc))
    
    return ans

def main():

    start_time = time.perf_counter()
    input = readInput()
    
    
    
    #print(findRolls(input))
    print(findRollsHash(input))
    end_time = time.perf_counter() 

    print(f"Time elapsed: {end_time - start_time:.6f} seconds")
if __name__ == "__main__":
    main()
