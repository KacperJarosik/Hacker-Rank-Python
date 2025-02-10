if __name__ == '__main__':
    n1 = int(input())
    data1 = set(input().split())
    n2 = int(input())
    data2 = set(input().split())
    print(len(data1.symmetric_difference(data2)))