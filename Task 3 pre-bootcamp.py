def num_check(x,y):
    z = x + y
    if z == 65:
        if x == 65 or y == 65:
            return True
    else:
        return False

print(num_check(65,0))
