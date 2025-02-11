"""
It works only in Python 2 because Python 3 generates different hashes, but the same tests are used for all versions.
"""


if __name__ == '__main__':
    n = int(raw_input())
    integer_tuple = tuple(map(int, raw_input().split()))
    print(hash(integer_tuple))
