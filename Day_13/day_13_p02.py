import re

def main():
    with open('input.txt','r') as infile:
        dots_input,instructions_input = infile.read().strip().split("\n\n")
        dots=set()
        instructions = list()
        for line in dots_input.strip().split("\n"):           
            x,y = line.strip().split(",")
            dots.add((int(x),int(y)))
    
        for line in instructions_input.strip().split("\n"):
            coord,value = re.search(r'^.*?(x|y)=(\d+)',line.strip()).groups()
            instructions.append((coord,int(value)))

    for coord,value in instructions:
        if coord == 'x':
            points_to_add = {entry for entry in dots if entry[0] > value}
            dots.update({((2*value) - x_val,y_val) for x_val,y_val in dots if x_val>value})
            dots = dots - points_to_add
        elif coord == 'y':            
            points_to_add = {entry for entry in dots if entry[1] > value}
            dots.update({(x_val, (2*value) - y_val) for x_val, y_val in dots if y_val>value})
            dots = dots - points_to_add          
    
    max_y = max(y for _,y in dots)
    max_x = max(x for x,_ in dots)

    for j in range(0,max_y+1):
        for i in range(0,max_x+1):
            if (i,j) in dots:
                print("█",end='')
            else:
                print(" ",end='')
        print()
       

if __name__ == '__main__':
    main()