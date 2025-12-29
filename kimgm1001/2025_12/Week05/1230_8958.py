def main():

    t = int(input())
    count = 0
    score = 0

    for _ in range(t):
        w = input()
        w = 'X' + w
        for i in range(1, len(w)):
            if w[i - 1] == 'X':
                for j in range(i, len(w)):
                    if w[j] == 'X':
                        break
                    count += 1
                    score += count
                count = 0
            else:
                continue
        print(score)
        score = 0

if __name__ == '__main__':
    main()