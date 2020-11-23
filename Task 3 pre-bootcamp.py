x = int(input("Please enter first number : "))
y = int(input("Please enter second number : "))
def num_check(x,y):
    z= x + y
    if z == 65:
        if x == 65 or y == 65:
            return True
    else:
        return False

print(num_check(x,y))
