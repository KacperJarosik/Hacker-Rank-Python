if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    output = []
    for x1 in range(x + 1):
        for y2 in range(y + 1):
            for z3 in range(z + 1):
                if (x1 + y2 + z3) != n:
                    output.append([x1, y2, z3])
    print(output)