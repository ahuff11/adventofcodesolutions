


def findrolls() -> int:
    file = "Day 4/input.txt"
    rolls = 0

    try:
        with open(file, 'r') as file:
            for line in file:  
                line = line.strip() 


        return rolls
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
        return 0
    

def main():
    print(findrolls)


if __name__ == "__main__":
    main()


# Brainstorm slop
# okay didnt realize this is a grid problem. The eight neighbors is the area that surrounds the grid. 
# i think a solution could be a bit map. 
# going to be n^2 no matter 
# i will probably have to pass through and save some sort of information then get the answer 
# holy shit can I use a 2d sliding window
# we loop through and we store current, topleft, topmid, topright, left, right, bottomleft, bottommid, bottom right