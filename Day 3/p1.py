import requests

# we can use ord function to compare the amounts of so we dont have to switch between string and int all the time

# whenever we get 99 that is our max and we can return from that loop

#iter_lines iterates through everyline to help memory when processing big inputs

# iterate right and check and compare if current right is bigger then max right
# also check if right is bigger than left if it is and we aren't at the end of our line set left to right
# also have another check where if left and right == 99 then we can end our loop early 
# if left == 9, then I just need to find the highest right
# i need an exit statement that when we hit our max voltage we exit this line and go to the next

def getJoltage() -> int:
    file = "Day 3/input.txt"
    voltage = 0
    try:
        with open(file, 'r') as file:
            for line in file:
                line = line.strip()

                l = line[0]
                lmax, rmax  = ord(l), ord('1')
                for c in range(1,len(line)):
                    
                    r = line[c]  
                    rmax = max(rmax, ord(r))
                    if l == '9' and r =='9':
                        break
                    elif lmax < rmax and c != len(line)-1:
                        l = r
                        lmax = ord(l)
                        r = line[c+1]
                        rmax = ord(r)
                    
                print(chr(lmax), chr(rmax))
                voltage += int(chr(lmax)+chr(rmax)) # O(n) however it will always be of size 2 which is constant so


        return voltage
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
        return 0





def main():

    print(getJoltage())

if __name__ == "__main__":
    main()