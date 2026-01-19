def main():

    import sys

    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    idx = 1

    for _ in range(t):
        k = int(data[idx])
        n = int(data[idx + 1])
        idx += 2
        
        
        people = [i for i in range(1, n + 1)]
        
        for _ in range(k):
            for j in range(1, n):
                people[j] += people[j - 1]
                
        print(people[-1])

if __name__ == '__main__':
    main()
