def main():

    w = list(input())
    result = []

    for i in w:
        if ord(i) > 91:
            result.append(chr(ord(i) - 32))
        else:
            result.append(chr(ord(i) + 32))

    print(''.join(result))

if __name__ == '__main__':
    main()