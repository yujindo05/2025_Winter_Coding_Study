def main():

    a = int(input())
    b = int(input())
    c = int(input())

    r = list(str(a * b * c))

    count = {'0' : 0, '1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0}

    for i in r:
        count[i] += 1

    for i in count.values():
        print(i)

if __name__ == '__main__':
    main()