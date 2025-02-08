if __name__ == '__main__':
    input_data = input()
    N, M = input_data.split()
    N = int(N)
    M = int(M)
    carpet = []
    for n in range(N):
        temp = ['-'] * M
        carpet.append(temp)
    for i in range(N // 2):
        for n in range(i,N-i):
            if n == N//2:
                continue
            carpet[n][M // 2 + 3 * i - 1] = '.'
            carpet[n][M // 2 + 3 * i] = '|'
            carpet[n][M // 2 + 3 * i + 1] = '.'
            carpet[n][M // 2 - 3 * i - 1] = '.'
            carpet[n][M // 2 - 3 * i] = '|'
            carpet[n][M // 2 - 3 * i + 1] = '.'
    carpet[N//2][M//2-3:M//2+4] = ['W','E','L', 'C', 'O', 'M', 'E']
    for n in range(N):
        print(''.join(carpet[n]))