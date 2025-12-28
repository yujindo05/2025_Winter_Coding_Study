def main():

    arr1 = []
    arr2 = []

    for i in range(28):
        arr1.append(int(input()))

    for i in range(1, 31):
        arr2.append(i)

    for i in arr2:
        if i not in arr1:
            print(i)

if __name__ == '__main__':
    main()