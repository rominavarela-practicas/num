import numpy as np
import sympy as sym

def get_symbols(N):
    X = []
    for i in xrange( 0 , N ):
        X.append( sym.Symbol( 'x'+str(i) ) )
    return X

def get_jacobian( functions , symbols ):
    # jacobian left side (derivates)
    jacobian_l = []
    for func in functions:
        sub = []
        for i in xrange( 0 , len(symbols) ):
            sub.append( sym.diff( func , symbols[i] , 1 ) )
        jacobian_l.append( sub )

    # jacobian right side (complements)
    jacobian_r = []
    for func in functions:
        jacobian_r.append( -func )

    return jacobian_l, jacobian_r

def lambdify( functions , symbols ):
    lambdas = []
    for f in functions:
        if type(f) is list:
            lambdas.append( lambdify( f , symbols ) )
        else:
            lambdas.append( sym.lambdify( symbols , f , ) )
    return lambdas

def solution( functions , coeficients , error ):
    ##########
    # SYMBOLIC INIT
    N = len(functions)
    coeficients = np.asarray(coeficients, dtype=float)
    symbols = get_symbols(N)
    jacobian_l, jacobian_r = get_jacobian( functions , symbols )

    ##########
    # LAMBDA INIT
    jacobian_l = lambdify( jacobian_l , symbols )
    jacobian_r = lambdify( jacobian_r , symbols )

    ##########
    # EVALUATION CYCLE
    left = np.zeros((N,N))
    right = np.zeros(N)
    e = 1

    while e > error:
        coeficients0 = np.copy(coeficients)

        # evaluation
        for row in xrange( 0 , N ):
            for col in xrange( 0 , N ):
                left[row][col] = jacobian_l[row][col](*coeficients)

        for row in xrange( 0 , N ):
            right[row] = jacobian_r[row](*coeficients)

        # inference
        for row in xrange( 0 , N ):
            val = right[row]
            for col in xrange( 0 , N ):
                if row != col:
                    val -= coeficients[col] * left[row][col]
            coeficients[row] = val / left[row][row]

        e = np.linalg.norm( coeficients - coeficients0 ) / np.linalg.norm ( coeficients )
        
    return coeficients
