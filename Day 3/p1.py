
def getJoltage() -> int:
    file = "Day 3/input.txt"
    voltage = 0
    try:
        with open(file, 'r') as file:
            for line in file:  #O(L) for line in file
                line = line.strip()

                l = line[0]
                lmax, rmax  = l, '1'
                for c in range(1,len(line)): #O(N) for character in line
                    
                    r = line[c]  
                    rmax = max(rmax, r)
                    if l == '9' and r =='9':    
                        break
                    elif lmax < rmax and c != len(line)-1:
                        l = r
                        lmax = l
                        r = line[c+1]
                        rmax = r
        
                voltage += int(lmax+rmax) #O(1) only has to change 2 letters so it becomes a constant.


        return voltage
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
        return 0

def main():

    print(getJoltage()) #O(L*N)
    
if __name__ == "__main__":
    main()