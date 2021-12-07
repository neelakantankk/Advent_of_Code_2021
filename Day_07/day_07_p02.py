from collections import Counter
from time import perf_counter_ns
import statistics

def main():   
    START = perf_counter_ns()
    with open('input.txt','r') as infile:
        alignments = [int(x) for x in infile.read().strip().split(',')]
    
    mean_position = round(statistics.mean(alignments))
    fuel_consumption_to_align = sum(sum(range(abs(alignment - mean_position)+1)) for alignment in alignments)
   
    print(fuel_consumption_to_align)
    STOP = perf_counter_ns()

    print(f"That took {(STOP - START)} nanoseconds")

if __name__ == '__main__':
    main()