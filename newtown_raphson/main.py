import numpy as np
import sympy as sym
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d;
import sys; sys.path.insert(0, './modules');
import newton_raphson;

x = sym.Symbol('x0')
y = sym.Symbol('x1')
z = sym.Symbol('x2')

f0 = x**2 + y**2 + z**2 -1
f1 = x**2 + z**2 - 0.25
f2 = x**2 + y**2 - 4*z

print newton_raphson.solution(
    functions = [ f0 , f1 , f2 ],
    x = [ 1 , 1 , 1 ],
    error = 0.7 )
