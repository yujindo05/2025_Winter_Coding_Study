def main():

    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    res = max((arr[i] + arr[j] + arr[k] for i in range(len(arr)) for j in range(len(arr)) for k in range(len(arr)) if i != j and j != k and i != k and arr[i] + arr[j] + arr[k] <= m))
    print(res)

if __name__ == '__main__':
    main()