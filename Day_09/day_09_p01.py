from collections import namedtuple
from time import perf_counter_ns

Point = namedtuple('Point',['x_pos','y_pos'])


def get_neighbors(pos,max_rows,max_cols):
    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    result = []

    for direction in directions:
        neighbor = Point(pos.x_pos + direction[0], pos.y_pos + direction[1])
        if 0 <= neighbor.x_pos < max_cols and 0 <= neighbor.y_pos < max_rows:
            result.append(neighbor)
    return result

def is_lower(pos,heights,max_rows,max_cols):
    adjacents = get_neighbors(pos, max_rows, max_cols)
    adjacent_heights = [heights[pos] for pos in adjacents]
    for height in adjacent_heights:
        if heights[pos] >= height:
            return False
    return True


def main():

    START = perf_counter_ns()
    
    with open('input.txt','r') as infile:
        heights = {Point(x_pos,y_pos):int(height) for y_pos,line in enumerate(infile.readlines()) for x_pos,height in enumerate(line.strip())}
        infile.seek(0)
        max_rows = len([line for line in infile.readlines()])
        infile.seek(0)
        max_cols = len(infile.readline().strip())
    
    total = 0
    
    for pos, height in heights.items():
        
        if is_lower(pos, heights, max_rows, max_cols):        
            total += (1 + height)            

    print(total)
    STOP = perf_counter_ns()
    print(f"Time taken: {STOP - START} nanoseconds")

if __name__ == '__main__':
    main()
