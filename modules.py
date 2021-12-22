import math as m
from numba import jit
from numpy import round as rd
from numpy import sqrt as sq
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
    dist = 0
    for it in range(0, iter):
        x_new, y_new = compl_n_calc(x, y, x_or, y_or)
        dist += dist_calc(x, y, x_new, y_new)
        x, y = x_new, y_new
        temp_module = module_calc(x, y)
        if temp_module > 4:
            break
        """temp_module = rd(module_calc(x, y), 6)
        if temp_module > 4:
            x_new, y_new = compl_n_calc(x, y, x_or, y_or)
            x_new, y_new = rd(x_new, 6), rd(y_new, 6)
            dist += dist_calc(x, y, x_new, y_new)
            break"""
    return (0, dist)

@jit(nopython=True)
def module_calc(x, y):
    dist = x**2 + y**2
    return dist

@jit(nopython=True)
def dist_calc(x, y, x_new, y_new):
    dist = sq((x-x_new)**2 + (y-y_new)**2)
    return dist

@jit(nopython=True)
def convert_speed(speed, iterations):
    return 4096 - round(4096*2**(-speed*2**-8)) - 1

@jit(nopython=True)
def convert_speed_2(speed):
    return round(1024/(1+e**(-speed+10)))

def main():
    speed = square_loop(4, -1, 0.8)
    print(convert_speed(speed))
    return 0

if __name__ == "__main__":
    main()
