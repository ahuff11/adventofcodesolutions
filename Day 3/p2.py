



#we can use like a heap we could loop through and once we hit size 12 for our jolts we can compare maybe
# loop through and find 
# we do a min heapq
# in the heap we append the leftmost high and save it as left most high  
# if i +12 = len(line)
# stack monotonic as long as the stinker is binker we add it 
# add elements to the stack if stack.size<12, if i+12 == len(line), if line[i] > stack.pop
# once we get towards the last elements in the stack we need to lock in the elements 

def getJoltage() -> int:
    file = "Day 3/input.txt"
    voltage = 0
     # stack will never be more then 12
    joltage = 12
    try:
        with open(file, 'r') as file:
            for line in file:  #O(L) for line in file
                line = line.strip()
                stack = []
                for i in range(len(line)-joltage):
                    while stack and line[i] > stack[-1]:
                        stack.pop()
                    if len(stack) < joltage+1:
                        stack.append(line[i])
                    
                print(stack)


        return voltage
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
        return 0

def main():

    print(getJoltage()) #O(L*N)
    
if __name__ == "__main__":
    main()