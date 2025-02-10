from collections import Counter

if __name__ == '__main__':
    n1 = int(input())
    magazine = Counter(input().split())
    n2 = int(input())
    money_earned = 0

    for _ in range(n2):
        item, price = input().split()
        if magazine[item] > 0:
            magazine[item] -= 1
            money_earned += int(price)

    print(money_earned)
