def bubble():
    list = [12, 34, 1, 64, 23, 5, 11, 2]
    for i in range(len(list)):
        print(i)
        for j in range(i):
            if list[i] < list[j]:
                list[j], list[i] = list[j], list[i]

            print(list)


s = bubble()
