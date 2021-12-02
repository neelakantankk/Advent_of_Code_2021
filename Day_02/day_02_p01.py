def parse_directions(direction, x_pos, y_pos):
    if direction[0] == 'forward':
        return (x_pos + int(direction[1]), y_pos)
    elif direction[0] == 'down':
        return (x_pos,y_pos + int(direction[1]))
    elif direction[0] == 'up':
        return (x_pos, y_pos - int(direction[1]))

def main():
    with open('input.txt','r') as infile:
        directions = [tuple(line.strip().split(" ")) for line in infile.readlines()]
    
    x_pos,y_pos = (0,0)

    for direction in directions:
        x_pos,y_pos = parse_directions(direction, x_pos, y_pos)
    
    print(x_pos * y_pos)
    

if __name__ == '__main__':
    main()