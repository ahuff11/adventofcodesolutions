

def getJoltage() -> int:
    file = "Day 3/input.txt"
    voltage = 0
    joltage = 12
    try:
        with open(file, 'r') as file:
            for line in file:  
                line = line.strip() 
                stack = []
                for i in range(len(line)): 
                    remaining = (len(line) - i)
                    while stack and line[i] > stack[-1] and remaining +len(stack) > joltage:
                        stack.pop()
                    if len(stack) < joltage:
                        stack.append(line[i])
    
                volt = "".join(stack)
                voltage += int(volt)
        
        return voltage
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
        return 0

def main():

    print(getJoltage()) #O(n) without considering reading input where n is the number of characters per line
                        # O(n * l) with reading input where l is the lines in input and n is the number if characters

if __name__ == "__main__":
    main()





# ---------------------------------------BRAINSTORM SLOP-----------------------------------------------------
# we can use like a heap we could loop through and once we hit size 12 for our jolts we can compare maybe
# loop through and find 
# we do a min heapq
# in the heap we append the leftmost high and save it as left most high  
# if i +12 = len(line)
# stack monotonic as long as it passes the condition then we add it 
# add elements to the stack if stack.size<12, if i+12 == len(line), if line[i] > stack.pop
# once we get towards the last elements in the stack we need to lock in the elements 
# what is the condition to where we can't add more numbers
# we could save a copy of the stack do the pop anyway and if its len(line) - i = how many elements are left. if after pop happens and the len of stack <12 then we go back to our copy and continue 