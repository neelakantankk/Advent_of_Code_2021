def main():
    with open('input.txt','r') as infile:
        bin_nums = [line.strip() for line in infile.readlines()]
    
    bit_len = len(bin_nums[0])

    gamma_rate = []
    epsilon_rate = []

    for i in range(0,bit_len):
        one_count, zero_count = (0,0)
        this_pos_bits = [num[i] for num in bin_nums]
        one_count = this_pos_bits.count('1')
        zero_count = this_pos_bits.count('0')

        if one_count > zero_count:
            gamma_rate.append('1')
            epsilon_rate.append('0')
        else:
            gamma_rate.append('0')
            epsilon_rate.append('1')
        
    gamma_rate = ''.join(gamma_rate)
    epsilon_rate = ''.join(epsilon_rate)

    print(int(gamma_rate,2)*int(epsilon_rate,2))
    

if __name__ == '__main__':
    main()