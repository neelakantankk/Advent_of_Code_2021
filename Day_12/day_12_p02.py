from queue import Queue
from time import perf_counter_ns

def get_all_paths(graph,node,destination,repeat_lower):
    visited = set()
    path = list()
    all_paths = set()
    repeat_visit = False
    def get_paths(graph, node,destination,visited,path, repeat_visit):
        if node in['start','end'] or (node.islower() and (node!=repeat_lower or repeat_visit == True)):
            visited.add(node)
        elif node == repeat_lower and repeat_visit == False:
            repeat_visit = True

        path.append(node)

        if node == destination:
            all_paths.add(tuple(path))
        else:
            for next_node in graph[node]:
                if next_node not in visited:
                    get_paths(graph, next_node, destination, visited, path, repeat_visit)
        path.pop()
        if node in['start','end'] or (node.islower() and (node!=repeat_lower or repeat_visit == True)):
            if node not in visited:
                repeat_visit == False
            else:
                visited.remove(node)

    get_paths(graph,node,destination,visited,path, repeat_visit)

    return all_paths


def main():
    START = perf_counter_ns()
    graph = dict()
    with open('input','r') as infile:
        for line in infile.readlines():
            caveA,caveB = line.strip().split("-")
            if caveA in graph:
                graph[caveA].append(caveB)
            else:
                graph[caveA] = [caveB]
            if caveB in graph:
                graph[caveB].append(caveA)
            else:
                graph[caveB] = [caveA]

    lowers = {key for key in graph.keys() if key.islower()}

    all_paths = set()
    for lower in lowers:
        all_paths.update(get_all_paths(graph, 'start','end',lower))

    print(len(all_paths))
    STOP = perf_counter_ns()
    INTERVAL = STOP - START

    print(f"Time taken: {INTERVAL} ns --> {INTERVAL/(10**9):.2f} seconds --> {INTERVAL/(10**6):.2f} ms")



if __name__ == '__main__':
    main()
