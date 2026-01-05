def main():

    import sys

    input = sys.stdin.readline

    n = int(input())
    arr = []

    for _ in range(n):
        a, b = input().split()
        arr.append([int(a), b])

    arr.sort(key = lambda x : x[0])

    for i in arr:
        print(i[0], i[1])

if __name__ == '__main__':
    main()