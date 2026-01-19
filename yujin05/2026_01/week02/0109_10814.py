def main():

    n = int(input())
    people = []

    for i in range(n):
        data = input().split()
        people.append ([int(data[0]),data[1]])

    for age in range(1,201):
        for person in people:
            p_age = person[0] 
            p_name = person[1]

            if p_age == age:
                print(p_age,p_name)

if __name__ == '__main__':
    main()
