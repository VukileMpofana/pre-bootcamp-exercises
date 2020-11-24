def time_converter(t):
    count = 0
    while t > 60:
            t = t - 60
            count = count + 1
    return str(count) + "H " + str(t) + "minutes"






print(time_converter(133))