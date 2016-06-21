import numpy as np
import sympy as sym
from matplotlib import pyplot as plt

x = sym.Symbol('x')

def zero( fx , a , tolerance):
    dx = sym.diff( fx , x , 1 );

    f = sym.lambdify(x, fx, "numpy")
    d = sym.lambdify(x, dx, "numpy")

    # find m within tolerance
    m = a - ( f(a) / d(a) )
    while f(m) is not 0 and abs(f(m)) > tolerance:
         m = a - ( f(a) / d(a) )
         a = m;
         
    return m
