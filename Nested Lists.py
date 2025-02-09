if __name__ == '__main__':
    dictionary = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dictionary[name] = score

    sorted_dict = sorted(dictionary.items(), key=lambda x: x[1])

    second_lowest_score = sorted(set(dictionary.values()))[1]
    result = []
    for key, value in dictionary.items():
        if value == second_lowest_score:
            result.append(key)
    for name in sorted(result):
        print(name)
