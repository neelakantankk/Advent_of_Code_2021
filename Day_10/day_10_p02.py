def total(completer):
    score = 0
    points = {
        ')':1,
        ']':2,
        '}':3,
        '>':4,
    }
    for char in completer:
        score = (score*5) + points[char]    
    return score

def main():
    with open('input.txt','r') as infile:
        syntax_lines = [line.strip() for line in infile.readlines()]
        
    corresponding_opener = {
        ')':'(',
        '}':'{',
        ']':'[',
        '>':'<',
    }
    corresponding_closer = {v:k for k,v in corresponding_opener.items()}
    scores = []

    for line in syntax_lines:
        stack = []
        is_corrupted = False
        for char in line:
            if char in [')','}',']','>']:
                if len(stack) == 0:
                    is_corrupted = True
                    break
                last_char = stack.pop()
                if last_char != corresponding_opener[char]:
                    is_corrupted = True
                    break
            else:
                stack.append(char)
        if is_corrupted:
            continue

        scores.append(total([corresponding_closer[char] for char in reversed(stack)]))
        
    print(sorted(scores)[(len(scores)//2)])

if __name__ == '__main__':
    main()