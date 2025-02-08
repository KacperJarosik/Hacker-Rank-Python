import textwrap

def wrap(string, max_width):
    output = ''
    while len(string) > max_width:
        if len(output) != 0:
            output += '\n'
        output += string[:max_width]
        string = string[max_width:]
    if len(string) !=0:
        output += '\n' + string
    return output
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)