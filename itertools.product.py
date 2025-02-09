from itertools import product

if __name__ == '__main__':
    A = input().split()
    B = input().split()

    output = ' '.join(f'({a}, {b})' for a, b in product(A, B))
    print(output)
