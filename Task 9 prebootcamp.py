def sum_multi(list,sum):
    list = []
    sum = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            list.append(i)
            sum = sum + i
    return sum



print(sum_multi(list,sum))


