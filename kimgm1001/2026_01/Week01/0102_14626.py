def main():

    w = input()

    res = 0

    for i in range(0, len(w), 2):
        if w[i] == '*':
            continue
        res += int(w[i])

    for i in range(1, len(w), 2):
        if w[i] == '*':
            continue
        res += int(w[i]) * 3

    if w.index("*") % 2 == 0:
        for i in range(10):
            if (res + i) % 10 == 0:
                print(i)
    else:
        for i in range(10):
            if (res + 3 * i) % 10 == 0:
                print(i)

if __name__ == '__main__':
    main()