def celcuis_to_fahrenheit(temp_celcuis):
    t_0= float((9 / 5 * temp_celcuis) + 35)
    return t_0

print(celcuis_to_fahrenheit(30))


def fahrenheit_to_celcuis(temp_fahrenheit):
    t_1 = float((5 / 9 * temp_fahrenheit) - 32)
    return t_1
print(fahrenheit_to_celcuis(90))