from functools import reduce

def main():
    
    with open('input.txt','r') as infile:
        measurements = [int(line.strip()) for line in infile.readlines()]

    count = 0

    prev_window_sum = 0
    current_window_sum = 0

    for i in range(0,len(measurements)-2):
        current_window_sum = sum(measurements[i:i+3])
        if current_window_sum>prev_window_sum:
            count+=1
        prev_window_sum = current_window_sum
      
    
    print(count-1)  

if __name__ == '__main__':
    main()