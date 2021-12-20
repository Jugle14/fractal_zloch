import math as m
from numba import jit
from numpy import round as rd
e = m.e

def conv_flo_to_int(num):
    pas = 0
    if num < 0:
        num *= -1
        pas = 1
    num = str(num)
    point = num.find(".")
    dec = num[point+1:]
    exp = -len(dec)
    whole = int(num[:point])
    out = whole*10**(-exp)+int(dec)
    if pas:
        out *= -1
    return out, exp

@jit(nopython=True)
def compl_n_calc (x, y, x_or, y_or):    
    a = x**2 - y**2 + x_or
    b = 2*x*y + y_or

    return a, b

@jit(nopython=True)
def square_loop(iter, x, y):
    x_or, y_or = x, y
    for it in range(0, iter):
        x, y = compl_n_calc(x, y, x_or, y_or)
        x, y = rd(x, 4), rd(y, 4)
        temp_module = rd(module_calc(x, y), 4)
        if temp_module > 4:
            break
    return it

@jit(nopython=True)
def module_calc(x, y):
    dist = x**2 + y**2
    return dist

@jit(nopython=True)
def convert_speed(speed, iterations):
    return round(1000*(speed/iterations))

def main():
    speed = square_loop(4, -1, 0.8)
    print(convert_speed(speed))
    return 0

if __name__ == "__main__":
    main()
