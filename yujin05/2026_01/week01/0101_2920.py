def main():

    m = list(map(int,input().split()))
    ascending = True
    descending = True
    for i in range(1,len(m)):
        if m[i] > m[i - 1] :
            descending = False
        elif m[i] < m[i-1]:
            ascending = False
    
    if ascending:
        print('ascending')
    elif descending:
        print('descending')
    else:
        print('mixed')
    
if __name__ == '__main__':
    main()