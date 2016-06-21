# import libraries
import numpy as np
import sympy as sym
from matplotlib import pyplot as plt

# import modules
import sys
sys.path.insert(0, './modules')
import bisection as bisection

# global
x = sym.Symbol('x')

# plot
def plot(X,Y,z):
    plt.plot( X , Y )
    plt.plot( X , np.zeros(len(Y)), 'k--' )
    plt.plot( z , 0, 'r*' )
    plt.title( ('a-b zero proximity visualization (z=' , z , ')' ))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

# user defined aproximation
def aprox( fx ):
    f = sym.lambdify(x, fx, "numpy")

    while True:
        print '\nAproximate a-b:'
        a = input('a: ');
        b = input('b: ');

        if f(a)*f(b) < 0:
            return a,b
        else:
            X = np.linspace(a,b,101);
            Y = f(X)
            plot(X,Y,0)

# main
def main():
    fx = sym.cos(x)
    a,b = aprox(fx)
    tolerance = input('tolerance: ')
    z = bisection.zero( fx , a , b , tolerance )

    # result
    f = sym.lambdify(x, fx, "numpy")
    print 'x=', z, ' y=', abs(f(z))
    print '    (zero)    (error)'

    # PLOT
    f = sym.lambdify(x, fx, "numpy")
    X = np.linspace(a,b,101);
    Y = f(X)
    plot(X,Y,z)

if __name__ == '__main__':
    main()
