def main():

    n = int(input())
    score = list(map(int,input().split()))
    ns = []

    m = max(score)

    for i in score:
        new = i/m*100
        ns.append(new)

    ave = sum(ns)/len(ns)
    print(ave)

if __name__ == '__main__':
    main()