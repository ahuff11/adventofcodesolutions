
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


