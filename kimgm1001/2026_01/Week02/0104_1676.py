def main():

    n = int(input())
    res = 1

    while n > 1:
        res *= n
        n -= 1

    count = 0
    temp = 1
    while True:
        temp *= 10
        if res % temp == 0:
            count += 1
            continue
        else:
            print(count)
            break

if __name__ == '__main__':
    main()