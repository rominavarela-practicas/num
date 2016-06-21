# import libraries
import numpy as np
import sympy as sym
from matplotlib import pyplot as plt

# import modules
import sys
sys.path.insert(0, './modules')
import newton_raphson as nr

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

    print '\nAproximate z:'
    a = input('Plot from: ');
    b = input('Plot to: ');
    X = np.linspace(a,b,101);
    Y = f(X)
    plot(X,Y,0)

    z = input('Aproximate zero: ');
    return z

# main
def main():
    fx = sym.cos(x)
    a = aprox(fx)
    tolerance = input('tolerance: ')
    z = nr.zero( fx , a , tolerance )

    # result
    f = sym.lambdify(x, fx, "numpy")
    print 'zero/x=', z, ' y/error=', abs(f(z))

    # PLOT
    f = sym.lambdify(x, fx, "numpy")
    X = np.linspace(- abs(z*a) , abs(z*a) ,101);
    Y = f(X)
    plot(X,Y,z)

if __name__ == '__main__':
    main()
