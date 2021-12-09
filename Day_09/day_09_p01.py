from collections import namedtuple
from time import perf_counter_ns

Point = namedtuple('Point',['x_pos','y_pos'])

def up_pos(point):
    return Point(point.x_pos, point.y_pos - 1)

def down_pos(point):
    return Point(point.x_pos, point.y_pos + 1)

def right_pos(point):
    return Point(point.x_pos +1, point.y_pos)

def left_pos(point):
    return Point(point.x_pos - 1, point.y_pos)

def is_lower(pos,heights,max_rows,max_cols):
    x_pos, y_pos = pos
    if x_pos == 0:
        if y_pos == 0:
            adjacents = [right_pos(pos), down_pos(pos)]
        elif y_pos == (max_rows - 1):
            adjacents = [right_pos(pos), up_pos(pos)]
        else:
            adjacents = [right_pos(pos), up_pos(pos), down_pos(pos)]
    elif x_pos == (max_cols - 1):
        if y_pos == 0:
            adjacents = [left_pos(pos), down_pos(pos)]
        elif y_pos == (max_rows - 1):
            adjacents = [left_pos(pos), up_pos(pos)]
        else:
            adjacents = [left_pos(pos), up_pos(pos), down_pos(pos)]
    else:
        if y_pos == 0:
            adjacents = [left_pos(pos), down_pos(pos), right_pos(pos)]
        elif y_pos == (max_rows - 1):
            adjacents = [left_pos(pos), up_pos(pos), right_pos(pos)]
        else:
            adjacents = [left_pos(pos), up_pos(pos), down_pos(pos), right_pos(pos)]
    
    adjacent_heights = [heights[pos] for pos in adjacents]
    
    for height in adjacent_heights:
        if heights[pos] >= height:
            return (False,None)
    
    return (True,adjacents)  

def main():

    START = perf_counter_ns()
    
    with open('input.txt','r') as infile:
        heights = {Point(x_pos,y_pos):int(height) for y_pos,line in enumerate(infile.readlines()) for x_pos,height in enumerate(line.strip())}
        infile.seek(0)
        max_rows = len([line for line in infile.readlines()])
        infile.seek(0)
        max_cols = len(infile.readline().strip())
    
    total = 0
    pos_to_skip = set()

    for pos, height in heights.items():
        
        if pos in pos_to_skip:
            continue

        is_pos_lower, adjacents = is_lower(pos, heights, max_rows, max_cols)

        if is_pos_lower:
            total += (1 + height)
            pos_to_skip.update(adjacents)

    print(total)
    STOP = perf_counter_ns()
    print(f"Time taken: {STOP - START} nanoseconds")

if __name__ == '__main__':
    main()