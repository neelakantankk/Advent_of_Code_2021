from time import perf_counter_ns

def get_neighbors(pos):
    directions = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]
    result = []
    for direction in directions:
        neighbor = (pos[0] + direction[0], pos[1] + direction[1])
        if (0 <= neighbor[0] < 10) and (0 <= neighbor[1] < 10):
            result.append(neighbor)
    return result

def get_flashers(octopuses):
    return [pos for pos,energy_value in octopuses.items() if energy_value > 9]

def main():
    START = perf_counter_ns()

    with open('input','r') as infile:
        octopuses = {(x,y):int(energy_value) for y,line in enumerate(infile.readlines()) for x,energy_value in enumerate(line.strip())}

    total_flashes = 0
    
    for step in range(0,100):
        for octopus_postion in octopuses:
            octopuses[octopus_postion] +=1

        flashers = get_flashers(octopuses)
        all_flashed = set()

        while len(flashers) > 0:
            for flasher in flashers:
                neighbors = get_neighbors(flasher)
                all_flashed.add(flasher)
                for neighbor in neighbors:
                    if neighbor not in all_flashed:
                        octopuses[neighbor] +=1
                octopuses[flasher] = 0   
            flashers = get_flashers(octopuses)

        for flashed in all_flashed:
            octopuses[flashed] = 0

        total_flashes += len(all_flashed)

    print(total_flashes)
    STOP = perf_counter_ns()

    print(f"Time taken: {STOP - START} ns")

if __name__ == '__main__':
    main()

