def main():
    with open('input.txt','r') as infile:
        output_values = [sides[1].split() for sides in (line.strip().split(" | ") for line in infile.readlines())]
    
    unique_output_values = [value for values in output_values for value in values if len(value) in [2,3,4,7]]      
    print(len(unique_output_values))

if __name__ == '__main__':
    main()