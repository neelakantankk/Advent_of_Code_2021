def main():
    with open('input.txt','r') as infile:
        syntax_lines = [line.strip() for line in infile.readlines()]
    
    illegal_characters = []
    corresponding_opener = {
        ')':'(',
        '}':'{',
        ']':'[',
        '>':'<',
    }
    points = {
        ')':3,
        ']':57,
        '}':1197,
        '>':25137,
    }

    for line in syntax_lines:
        stack = []
        for char in line:
            if char in [')','}',']','>']:
                if len(stack) == 0:
                    illegal_characters.append(char)
                    break
                last_char = stack.pop()
                if last_char != corresponding_opener[char]:
                    illegal_characters.append(char)
                    break
            else:
                stack.append(char)
    
    total = sum(points[char] for char in illegal_characters)
    print(total)   

if __name__ == '__main__':
    main()