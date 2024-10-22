from math import ceil

def square(side):
    s = side * side
    return s

side = float(input("Длина стороны квадрата: "))
result = square(side)
rounded_result = ceil(result)
print(f'Округленная в большую сторону сумма - {rounded_result}')
