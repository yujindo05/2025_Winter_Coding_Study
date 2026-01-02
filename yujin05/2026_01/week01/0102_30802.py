def main():
    n = int(input())
    size = list(map(int,input().split()))
    tp =list( map(int,input().split()))
    tr = 0
    for i in size:
        t = i // tp[0]
        if i % tp[0] !=0:
            t += 1
            tr += t
        else: 
            tr += t
    print(tr)
    
    p = n // tp[1]
    pi = n % tp[1]
    print(p,pi)    

if __name__ == '__main__':
    main()