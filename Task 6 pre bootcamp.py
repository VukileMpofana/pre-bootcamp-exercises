#x = input("enter first number : ")
#y = input("Enter second number : ")
#z = input("enter third number : ")

def max_num(x,y,z):
    if x > y and z:
        return x
    elif y > z:
        return y
    else:
        return z

print(max_num(10,20,30))