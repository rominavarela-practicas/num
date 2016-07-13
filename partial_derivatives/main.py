import numpy as np
import sympy as sym
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d;
import sys; sys.path.insert(0, './modules');
import rk4;

t = sym.Symbol('x0')
x = sym.Symbol('x1')
y = sym.Symbol('x2')
z = sym.Symbol('x3')

dx_dt = 10 * ( x + y )
dy_dt = ( 2.8 * x ) - y - ( x * z )
dz_dt = ( x * y ) - ( 8.0 / 3.0 * z )

T , X = rk4.next_n (
    functions = [ dx_dt , dy_dt , dz_dt ] ,
     t0 = 0 ,
     x0 = [ 10 , 7 , 7 ] ,
     h = 0.001 ,
     n = 100 )

# PLOT
plt.plot( X[0] , T , 'k')
plt.plot( X[1] , T , 'b')
plt.plot( X[2] , T , 'm')

plt.xlabel('X')
plt.ylabel('T')
plt.show()
