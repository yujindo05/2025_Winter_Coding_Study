def main():
    a = int(input())
    b = int(input())
    c = int(input())
    multi = str(a*b*c)
    n ='0123456789'

    for j in n:
        count = 0 
        for i in multi:
            if i == j:
                count += 1
        print(count)
    
if __name__ == '__main__':
    main()