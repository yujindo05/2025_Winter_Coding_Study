def main():

    a, b, c, d, e = map(int, input().split())

    r = (a**2 + b**2 + c**2 + d**2 + e**2) % 10

    print(r)

if __name__ == '__main__':
    main()