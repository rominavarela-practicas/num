# http://fourier.eng.hmc.edu/e161/lectures/ica/node13.html
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
@param functions[]
@param symbols[]
@returns symbolic function matrix
"""
def get_jacobian( functions , symbols ):
    jacobian = []
    for func in functions:
        sub = []
        for i in xrange( 0 , len(symbols) ):
            sub.append( sym.diff( func , symbols[i] , 1 ) )
        jacobian.append( sub )

    return jacobian

"""
@param symbolic functions[]
@param symbols[]
@returns lambda functions
"""
def lambdify( functions , symbols ):
    lambdas = []
    for f in functions:
        if type(f) is list:
            lambdas.append( lambdify( f , symbols ) )
        else:
            lambdas.append( sym.lambdify( symbols , f , ) )
    return lambdas

"""
@param lambda functions[]
@param function arguments/coeficients[]
@returns lambda functions
"""
def evaluate( functions , coeficients ):
    eval = []
    for f in functions:
        if type(f) is list:
            eval.append( evaluate( f , coeficients ) )
        else:
            eval.append( f(*coeficients) )
    return eval

"""
@param functions[] where number of elements = N
@param coeficients[] where number of elements = N
@returns newton-raphson solution
"""
def solution( functions , x , error , maxit=100):
    ##########
    # SYMBOLIC INIT
    N = len(functions)
    symbols = get_symbols(N)
    jacobian = get_jacobian( functions , symbols )

    ##########
    # TO LAMBDA
    functions = lambdify( functions , symbols )
    jacobian = lambdify( jacobian , symbols )

    e = error + 1
    for i in xrange(0,maxit):
        ##########
        # EVALUATION
        x0 = np.asarray(x, dtype=float)
        f = evaluate( functions , x0 )
        j = evaluate( jacobian , x0 )
        j = np.linalg.inv(j)

        for xi,terms in enumerate( np.multiply(j,f) ):
            x[xi] = x0[xi] - terms.sum()

        # ERROR
        e = np.linalg.norm( x - x0 ) / np.linalg.norm ( x )
        print "e = " , e
        if e <= error: break

    print ' '
    return x
