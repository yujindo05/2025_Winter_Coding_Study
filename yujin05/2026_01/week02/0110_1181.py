def main():

    import sys

    n = int(sys.stdin.readline())
    word = []
    for i in range(n):
        x = sys.stdin.readline().strip()
        word.append(x)

    word = list(set(word))
    new= []
    for j in word :
        new.append((len(j),j))

    new.sort()
    for length, j in new:
        print(j)

if __name__ == '__main__':
    main()
