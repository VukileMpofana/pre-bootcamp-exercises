x = int(input("enter your number : "))
y = int(input("enter your second number : "))

def num_check(x,y):
    z = x + y
    list = [int(i) for i in str(z)]
    if x == 3 or y == 3:
        if 3 in list:
            return True
    else:
        return False
print(num_check(x,y))