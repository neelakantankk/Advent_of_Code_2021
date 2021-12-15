import heapq
from time import perf_counter_ns

def get_neighbors(node, graph):
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    results = []
    for direction in directions:
        neighbor = (node[0] + direction[0],node[1] + direction[1])
        if neighbor in graph:
            results.append(neighbor)
    return results

def manhattan_distance(begin, end):
    x1,y1 = begin
    x2,y2 = end
    return abs(x1-x2) + abs(y1 - y2)

def find_lowest_risk(graph, begin,end):
    frontier = []
    heapq.heappush(frontier,(0,begin))
    risk_so_far = dict()
    risk_so_far[begin] = 0

    while frontier:
        current = heapq.heappop(frontier)[1]

        if current == end:
            break

        for neighbor in get_neighbors(current, graph):
            new_risk = risk_so_far[current] + graph[neighbor]
            if neighbor not in risk_so_far or new_risk < risk_so_far[neighbor]:
                risk_so_far[neighbor] = new_risk
                priority = new_risk + manhattan_distance(neighbor,end)
                heapq.heappush(frontier,(priority,neighbor))

    return risk_so_far[end]

def new_cost(old_cost):
    if old_cost+1>9:
        return 1
    else:
        return old_cost+1

def main():
    START = perf_counter_ns()
    with open("input",'r') as infile:
        graph = {(x,y):int(cost) for y,line in enumerate(infile.readlines(),1) for x,cost in enumerate(line.strip(),1)}

    prev_y_index = 0
    to_add = max(x for x,y in graph.keys())

    for y_rep in range(1,5):
        new_graph = {(key[0],key[1]+to_add):new_cost(cost) for key,cost in graph.items() if key[1]>prev_y_index}
        graph.update(new_graph)
        prev_y_index += to_add

    prev_x_index = 0
    for x_rep in range(1,5):
        new_graph = {(key[0]+to_add,key[1]):new_cost(cost) for key,cost in graph.items() if key[0]>prev_x_index}
        graph.update(new_graph)
        prev_x_index += to_add


    begin = (1,1)
    end = (max(x for x,y in graph.keys()),max(y for x,y in graph.keys()))
    
    lowest_risk = find_lowest_risk(graph, begin, end)
    print(lowest_risk)
    STOP = perf_counter_ns()
    INTERVAL = STOP - START
    print(f"Time taken: {INTERVAL} ns = {INTERVAL/(10**6):.2f} ms = {INTERVAL/(10**9):.2f} s")

if __name__ == '__main__':
    main()
