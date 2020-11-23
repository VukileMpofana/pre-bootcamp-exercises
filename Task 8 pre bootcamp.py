#t = int(input("enter any random number : "))

def time_converter(t):
    count = 0
    while t > 60:
            t = t - 60
            count = count + 1
    print(str(count) + "H " + str(t) + " minutes")


print(time_converter(71))