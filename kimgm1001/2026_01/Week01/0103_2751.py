def main():

    import sys

    input = sys.stdin.readline

    n = int(input())

    arr1 = ['*'] * 1000001
    arr2 = ['*'] * 1000000

    for _ in range(n):
        num = int(input())
        if num >= 0:
            arr1[num] = num
        else:
            arr2[num] = num

    for i in arr2:
        if i != '*':
            print(i)
    for i in arr1:
        if i != '*':
            print(i)

if __name__ == '__main__':
    main()