# import libraries
import numpy as np
import sympy as sym
from matplotlib import pyplot as plt

# import modules
import sys; sys.path.insert(0, './modules');
import integration

# fx
x = sym.Symbol('x')
fx = abs(sym.cos(x))
f = sym.lambdify(x, fx, "numpy")

# x , y
a = 0;
b = 10;
X = np.linspace(a,b,91)
Y = f(X)

print '\ntrapezoidal:'
print integration.trapezoidal(X,Y)

print '\ncomposed trapezoidal increasing hops:'
print integration.comp_trapezoidal(X,Y,len(X)//10), '    1/10 hops'
print integration.comp_trapezoidal(X,Y,len(X)-1), '    max hops'

print '\nsimpson 1/3:'
print integration.simpson_1_3(X,Y)

print '\nsimpson 3/8:'
print integration.simpson_3_8(X,Y)

# PLOT 1/10
plt.plot( X[::10] , Y[::10] , 'k')

for x in X[::10]:
    plt.plot( [x,x] , [0,f(x)] , 'g')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('1/10 hops')
plt.show()

# PLOT max
plt.plot( X , Y , 'k')

for x in X:
    plt.plot( [x,x] , [0,f(x)] , 'm')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('max hops')
plt.show()
