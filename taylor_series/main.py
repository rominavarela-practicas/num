# import libraries
import numpy as np
import sympy as sym
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d;

# import modules
import sys; sys.path.insert(0, './modules');
import taylor

# f(x,y)
x = sym.Symbol('x')
y = sym.Symbol('y')
f = y * sym.exp( x )

a = 0
b = 0
order = 1
fig = plt.figure();
ax = fig.add_subplot(111, projection='3d');
X, Y, Z = axes3d.get_test_data(0.05)

while order < 11 :

    t= taylor.solution( f , a , b , order )
    order += 1
    print '\n\norder ' , order
    print t

    # plot
    t = sym.lambdify( [x,y] , t , "numpy")
    solution = t(X,Y)
    if order < 11 :
        ax.plot_wireframe(X, Y, solution, rstride=10, cstride=10, color='m')
    else :
        ax.plot_wireframe(X, Y, solution, rstride=10, cstride=10, color='b')

# PLOT
f = sym.lambdify( [x,y] , f , "numpy")
F = f(X,Y)
ax.plot_wireframe(X, Y, F, rstride=10, cstride=10, color='k')
plt.show()
