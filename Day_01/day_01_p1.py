from functools import reduce

def main():
    
    with open('input.txt','r') as infile:
        measurements = [int(line.strip()) for line in infile.readlines()]

    count = 0

    for i in range(0,len(measurements)-1):
        if measurements[i+1] > measurements[i]:
            count+=1
    
    print(count)  

if __name__ == '__main__':
    main()