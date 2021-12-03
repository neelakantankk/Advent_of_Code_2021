def get_num(bin_nums,gas):
    nums = bin_nums.copy()
    bit_len = len(bin_nums[0])
    for i in range(0,bit_len):
        one_count, zero_count = (0,0)
        this_pos_bits = [num[i] for num in nums]
        one_count = this_pos_bits.count('1')
        zero_count = this_pos_bits.count('0')

        if gas == 'o2':
            if one_count >= zero_count:
                required_bit = '1'
            else:
                required_bit = '0'
        else:
            if one_count >= zero_count:
                required_bit = '0'
            else:
                required_bit = '1'
        
        req_nums = [num for num in nums if num[i] == required_bit]
        if len(req_nums) == 1:
            return int(''.join(req_nums[0]),2)
        else:
            nums = req_nums
        
def main():
    with open('input.txt','r') as infile:
        bin_nums = [line.strip() for line in infile.readlines()]    

    o2_num = get_num(bin_nums,'o2')
    co2_num = get_num(bin_nums,'co2')

    print(o2_num * co2_num)    

if __name__ == '__main__':
    main()