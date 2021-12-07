from collections import Counter
from time import perf_counter_ns

def main():   
    START = perf_counter_ns()
    with open('input.txt','r') as infile:
        alignments = [int(x) for x in infile.read().strip().split(',')]
    
    possible_positions = range(min(alignments),max(alignments)+1)

    min_fuel_consumption = None
    
    for number in possible_positions:
        fuel_consumption_to_align = sum(sum(range(abs(alignment - number)+1)) for alignment in alignments)        
        if min_fuel_consumption is None or min_fuel_consumption > fuel_consumption_to_align:
            min_fuel_consumption = fuel_consumption_to_align

    print(min_fuel_consumption)   
    STOP = perf_counter_ns()

    print(f"That took {(STOP - START)/1000} seconds")

if __name__ == '__main__':
    main()