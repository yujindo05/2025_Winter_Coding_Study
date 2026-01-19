def main():

    import sys

    x = int(sys.stdin.readline())

    n = 1
    max = 1

    while x > max:
        max += 6 * n
        n += 1

    print(n)

if __name__ == '__main__':
    main()
