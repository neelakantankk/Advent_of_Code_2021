from collections import Counter
import statistics

def main():   
    with open('input.txt','r') as infile:
        alignments = [int(x) for x in infile.read().strip().split(',')]
    
    median_position = round(statistics.median(alignments))
    fuel_consumption_to_align = sum(abs(alignment - median_position) for alignment in alignments)   
    print(fuel_consumption_to_align)

if __name__ == '__main__':
    main()