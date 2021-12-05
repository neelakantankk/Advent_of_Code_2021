def same_x(start,end):
    if start[1] > end[1]:
        return ((start[0],x) for x in range(end[1],start[1]+1))
    else:
        return ((start[0],x) for x in range(start[1], end[1]+1))

def same_y(start,end):
    if start[0] > end[0]:
        return ((x,start[1]) for x in range(end[0], start[0]+1))
    else:
        return ((x,start[1]) for x in range(start[0],end[0]+1))

def diagonal(start,end):
    if start[0] > end[0] and start[1] > end[1]:
        return zip(range(end[0],start[0]+1),range(end[1],start[1]+1))
    elif start[0] < end[0] and start[1] < end[1]:
        return zip(range(start[0],end[0]+1),range(start[1],end[1]+1))
    elif start[0] < end[0] and start[1]>end[1]:
        return zip(range(start[0],end[0]+1), range(start[1],end[1]-1,-1))
    elif start[0] > end[0] and start[1] < end[1]:
        return zip(range(start[0],end[0]-1,-1), range(start[1],end[1]+1))

def main():
    with open('input','r') as infile:
        data = [line.strip().split(" -> ") for line in infile.readlines()]
        vents = list(map(lambda x: [tuple(int(i) for i in x[0].split(",")),tuple(int(i) for i in x[1].split(","))],data))
    
    total_points_covered = set()
    overlaps = set()

    for vent in vents:
        start, end = vent
        if start[0] == end[0]:
            points_covered_by_this_vent = same_x(start,end)
        elif start[1] == end[1]:
            points_covered_by_this_vent = same_y(start,end)
        else:
            points_covered_by_this_vent = diagonal(start,end)

        for point in points_covered_by_this_vent:
            if point in total_points_covered:
                overlaps.add(point)
            else:
                total_points_covered.add(point)

    print(len(overlaps))




if __name__ == '__main__':
    main()
