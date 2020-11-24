def num_check(x,y):
    z = x + y
    list = [int(i) for i in str(z)]
    if x == 3 or y == 3:
        if 3 in list:
            return True
    else:
        return False
print(num_check(0,3))