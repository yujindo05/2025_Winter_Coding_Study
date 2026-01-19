def main():

    n, k = map(int,input().split())

    def factorial(x):
        a = 1
        for i in range(2, x+1):
            a *= i
        return a

    print(factorial(n)//(factorial(k) * factorial(n-k)))

if __name__ == '__main__':
    main()
