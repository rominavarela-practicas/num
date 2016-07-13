import numpy as np
import sympy as sym

"""
@param N
@returns x0, x1 ... xN symbols
"""
def get_symbols(N):
    X = []
    for i in xrange( 0 , N ):
        X.append( sym.Symbol( 'x'+str(i) ) )
    return X

"""
@param symbols[]
@param symbolic functions[]
@returns lambda functions
"""
def lambdify( symbols , functions ):
    lambdas = []
    for f in functions:
        if type(f) is list:
            lambdas.append( lambdify( symbols , f) )
        else:
            lambdas.append( sym.lambdify( symbols , f , ) )
    return lambdas

def next_n ( functions , t0 , x0 , h , n ):
    symbols = get_symbols( 1 + len(x0) )
    lambdas = lambdify( symbols , functions )

    t = t0
    x = np.asarray( x0 , dtype=float )

    # first push
    TList = [ t ]
    XList = []
    xiterator = range(0,len(x0))
    for xi in xiterator:
        XList.append([ x0[xi] ])

    for i in xrange(0,n):
        t , x = next ( lambdas , t , x , h )
        TList.append(t)
        for xi in xiterator:
            XList[xi].append(x[xi])

    return TList,XList

"""
@param f[] lambda funcions
@param t0 independient variable
@param x0[] dependient variables
@param h hop size
@returns next t0 and x0 later in +h
"""
def next ( f , t0 , x0 , h ):
    n = len(x0)
    iterator = range(0,n)

    # k1
    ti = t0
    xi = np.copy( x0 )
    k1 = np.zeros(n)
    for i in iterator:
        k1[i] = h * f[i]( ti , *xi)

    # k2
    k2 = np.zeros(n)
    ti = t0 + (h/2)
    for i in iterator:
        xi[i] = x0[i] + (k1[i]/2)

    for i in iterator:
        k2[i] = h * f[i]( ti , *xi)

    # k3
    k3 = np.zeros(n)
    ti = t0 + (h/2)
    for i in iterator:
        xi[i] = x0[i] + (k2[i]/2)

    for i in iterator:
        k3[i] = h * f[i]( ti , *xi)

    # k4
    k4 = np.zeros(n)
    ti = t0 + h
    for i in iterator:
        xi[i] = x0[i] + k3[i]

    for i in iterator:
        k4[i] = h * f[i]( ti , *xi)

    # solution
    ti = t0 + h
    xi = np.copy( x0 )
    for i in iterator:
        xi[i] += ( k1[i] + 2*k2[i] + 2*k3[i] +k4[i] ) / 6.0

    return ti , xi
