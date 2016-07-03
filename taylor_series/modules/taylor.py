import numpy as np
import sympy as sym

x = sym.Symbol('x')
y = sym.Symbol('y')

def series_triangle(N):
    N+=1;
    triangle = np.zeros( (N,N) );

    for i in xrange(1,N):
        for j in xrange(0,i):
            triangle[i][j]= j+1;

    return triangle

def pascal_triangle(N):
    N+=1;
    triangle = np.zeros( (N,N) , dtype=int );

    for i in xrange(0,N):
        for j in xrange(0,i+1):
            if i == 0:
                triangle[i][j]= 1;
            elif j == 0:
                triangle[i][j]= triangle[i-1][j]
            else:
                triangle[i][j]= triangle[i-1][j] + triangle[i-1][j-1]

    return triangle

def sub_solution( f , a , b , order , factors ):
    sub = 0

    for i in xrange( 0 , order+1 ):
        factor = factors[i]
        xi = order-i
        yi = i

        # derivation
        dx = sym.diff( f , x , xi );
        dxy = sym.diff( dx , y , yi );
        subs = dxy.subs( x , a );
        subs = subs.subs( y , b );

        # sub function concat
        sub += factor * ( (x-a) ** xi ) * ( (y-b) ** yi ) * subs

    return sub

# Taylor solution
def solution( f , a , b , order ):
    t = 0 # taylor funcion
    series = series_triangle(order);
    pascal = pascal_triangle(order);

    for order_i in xrange(1,order+1):

        factors = pascal[order_i][:order_i+1]
        sub = sub_solution( f , a , b , order_i , factors )
        t += ( ( 1 / series[order_i].sum() ) * sub )

    return t
