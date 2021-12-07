from collections import Counter
from functools import reduce

def main():   
    with open('input.txt','r') as infile:
        alignments = [int(x) for x in infile.read().strip().split(',')]
    
    count_of_alignments = Counter(alignments)

    min_fuel_consumption = None
    
    for number,count in count_of_alignments.most_common():
        fuel_consumption_to_align = sum(abs(alignment - number) for alignment in alignments)
        if min_fuel_consumption is None or min_fuel_consumption > fuel_consumption_to_align:
            min_fuel_consumption = fuel_consumption_to_align

    print(min_fuel_consumption)

if __name__ == '__main__':
    main()