def main():

    n = int(input())

    # for i in range(1, n + 1):
    #     if i + sum(map(int, str(i))) == n:
    #         print(i)
    #         exit()
    #
    # print(0)

    i = max(0, n-53)

    while i + sum(map(int, str(i))) != n and i < n:
        i += 1

    if i != n:
        print(i)
    else:
        print(0)

if __name__ == '__main__':
    main()