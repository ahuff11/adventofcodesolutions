# Time Complexity = O(n) where n is the number of lines in the input file
# Space Complexity = O(1)
# Time Complexity could be viewed as O(n*d) where n is the number of lines and d is the number of digits in the largest number
# However, largest input is 4 digits which is a constant. If input were to grow digit size then we would have O(n*d)
    
def findDial() ->int:
    dial = 50
    count = 0
    file_path = 'input.txt'

    try:
        with open(file_path, 'r') as file:
            for line in file:
                processed_line = line.strip()
                number = int(processed_line[1:]) 
                crossedzero = 0
              
                if processed_line[0] == "R":
                    crossedzero = (dial+number)//100
                    count += crossedzero
                    dial = (dial+number) % 100
                  
                else:    
                    if dial == 0:
                        count += number //100
                    elif number >= dial:
                        count += (number-dial)//100 +1
                    dial = (dial-number) % 100

        return count         
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return 0
    

def main():
    print(findDial())


if __name__ == "__main__":
    main()

