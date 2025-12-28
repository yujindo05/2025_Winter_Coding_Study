def main():

    n = int(input())
    r = 1

    if n == 0:
        print(r)
    else:
        for i in range(n):
            r *= (i + 1)
        print(r)

if __name__ == '__main__':
    main()