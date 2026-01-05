import sys

def main():

    n = int(input())
    arr = list(set(sys.stdin.readline().strip() for _ in range(n)))

    # count1 = 0
    # count2 = 0
    # arr.sort()
    #
    # while True:
    #     count1 += 1
    #     for i in arr:
    #         if len(i) == count1:
    #             print(i)
    #             count2 += 1
    #     if count2 == len(arr):
    #         break

    arr.sort(key = lambda x : (len(x), x))

    for i in arr:
        print(i)

if __name__ == '__main__':
    main()