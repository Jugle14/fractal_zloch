import math as m
from numba import jit
from numpy import sqrt as sq, log10 as log, log2
from values import increasing

escape_module = 4
escape_module *= 10**increasing

def conv_flo_to_int(num):
    pas = 0
    if num < 0:
        num *= -1
        pas = 1
    num = str(num)
    exp = 0
    point = num.find(".")
    
    for i in num[point+1]:
        if i == "0":
            exp -= 1
        else:
            break
    dec = num[point+1-exp:]
    e_p = dec.find("e")
    if e_p != -1:
        exp += int(dec[e_p+1:])
        dec = dec[:e_p]
    exp -= len(dec)
    whole = int(num[:point] + dec[:e_p])
    out = whole*10**(-exp)+int(dec)
    if pas:
        out *= -1
    return out, exp

@jit(nopython=True)
def compl_n_calc (x, y, x_or, y_or):    
    a = (x**2 - y**2)/(10**increasing) + x_or
    b = (2*x*y)/(10**increasing) + y_or
    return a, b

@jit(nopython=True)
def square_loop(iter, x, y):
    x_or, y_or = x, y
    # convert float to int and exponent number
    for it in range(1, iter+1):
        x, y = compl_n_calc(x, y, x_or, y_or) # give only int
        temp_module = module_calc(x, y) # also give exponent
        if temp_module/(10**increasing) > escape_module:
            break
    var_temp = log2(sq(module_calc(x, y)))
    var_temp = 10 if var_temp < 0 else var_temp
    it += 1 - log(var_temp)
    return it

@jit(nopython=True)
def module_calc(x, y):
    dist = (x**2) + (y**2)
    return dist

@jit(nopython=True)
def dist_calc(x, y, x_new, y_new):
    dist = sq((x-x_new)**2 + (y-y_new)**2)
    return dist

@jit(nopython=True)
def convert_speed(speed, iterations):
    return int(255*speed/iterations)
