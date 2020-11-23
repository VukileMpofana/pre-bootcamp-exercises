def temp_convert(t_d):
    t_f = float((9 / 5 * t_d) + 35)
    return t_f

print(temp_convert(30))


def temp_convert_1(t_f):
    deg = float((5 / 9 * t_f) - 32)
    return deg
print(temp_convert_1(90))