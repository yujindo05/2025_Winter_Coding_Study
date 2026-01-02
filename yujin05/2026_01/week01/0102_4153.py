def main():

    while True: 
        tri = list(map(int,input().split()))
        tri.sort()
        if tri != [0,0,0]:
            if tri[-1]**2 == tri[0]**2+tri[1]**2:
                print('right')
            else:
                print('wrong') 
        else:
            break
if __name__ == '__main__':
    main()

    # sort() : 매서드-> 오름차순으로 정리