from time import perf_counter_ns

def main():

    START = perf_counter_ns()

    with open('input.txt','r') as infile:
        pair_insert = dict()
        pair_count = dict()
        base,data = infile.read().strip().split("\n\n")
        for line in data.split("\n"):
            pair, insert = line.strip().split(" -> ")
            pair_insert[pair] = insert
                
    base_pairs = [f"{base[index]}{base[index+1]}" for index in range(0,len(base)-1)]
    pair_count = dict()
    for pair in base_pairs:
        count = pair_count.setdefault(pair,0)
        pair_count[pair] = count + 1
 
    END = 10
    counts = dict()
    for step in range(0,END):
        new_pairs = dict()        
        
        for pair, count in pair_count.items():
            new_first = f"{pair[0]}{pair_insert[pair]}"            
            first_count = new_pairs.setdefault(new_first,0)

            new_second = f"{pair_insert[pair]}{pair[1]}"
            second_count = new_pairs.setdefault(new_second,0)

            new_pairs[new_first] = first_count + count
            new_pairs[new_second] = second_count + count
        
        pair_count = new_pairs
    
    characters = {char for key in pair_count.keys() for char in key} 

    for character in characters:
        character_count = sum(pair.count(character)*pair_count[pair] for pair in pair_count)
        counts[character] = character_count//2
    counts[base[-1]] +=1
    counts[base[0]] +=1

    max_count = max(counts.values())
    min_count = min(counts.values())
    print(max_count - min_count)

    STOP = perf_counter_ns()
    INTERVAL = STOP - START
    print(f"Time Taken: {INTERVAL} ns == {INTERVAL/(10**6):.2f} ms == {INTERVAL/(10**9):.2f} s")

if __name__ == '__main__':
    main()