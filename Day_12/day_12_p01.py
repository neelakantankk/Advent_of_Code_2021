from queue import Queue

def get_all_paths(graph,node,destination):
    visited = set()
    path = list()
    all_paths = list()
    def get_paths(graph, node,destination,visited,path):
        if node.islower():
            visited.add(node)
        path.append(node)

        if node == destination:
            all_paths.append(path.copy())
        else:
            for next_node in graph[node]:
                if next_node not in visited:
                    get_paths(graph, next_node, destination, visited, path)
        path.pop()
        if node.islower():
            visited.remove(node)


    get_paths(graph,node,destination,visited,path)

    return all_paths


def main():
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

    all_paths = get_all_paths(graph, 'start','end')
    print(len(all_paths))



if __name__ == '__main__':
    main()
