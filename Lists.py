if __name__ == '__main__':
    N = int(input())
    list1 = []

    for _ in range(N):
        command = input().split()
        operation = command[0]
        args = list(map(int, command[1:]))

        if operation == "print":
            print(list1)
        else:
            getattr(list1, operation)(*args)
