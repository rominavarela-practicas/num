import numpy as np
import sympy as sym
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d;
import sys; sys.path.insert(0, './modules');
import newton_raphson;

x0 = sym.Symbol('x0')
x1 = sym.Symbol('x1')

f0 = ( x0 ** 2 ) - ( 10 * x0 ) + ( x1 ** 2 ) + 8
f1 = ( x0 * x1 ** 2 ) + x0 - ( 10 * x1 ) + 8
print newton_raphson.solution(
    functions = [ f0 , f1 ],
    coeficients = [ 0 , 0 ],
    error = 0.7 )
