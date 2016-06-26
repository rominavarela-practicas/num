def trapezoidal( X , Y ):
    a = X[0]
    b = X[-1]
    fa = Y[0]
    fb = Y[-1]
    return ( b - a ) * ( (fa + fb) / 2 );

# count of X % n must be 0
def comp_trapezoidal( X , Y , n ):
    if (len(X)-1) % n : return None

    # cache
    h = (len(X)-1)/n
    accum = 0

    # sum n trapezoids
    for i in xrange(0,n):
        a = X[i*h];
        b = X[(i+1)*h];
        fa = Y[i*h];
        fb = Y[(i+1)*h];

        sub = ( b - a ) * ( (fa + fb) / 2 );
        accum += sub;

    return accum

# count of X % 2 must be 0
def simpson_1_3( X , Y ):
    if (len(X)-1) % 2 : return None

    a = X[0]
    b = X[-1]
    n = len(X)-1
    h = float(b-a)/n

    sum_1 = sum(Y[ 1 : len(X)-1 : 2 ])
    sum_2 = sum(Y[ 2 : len(X)-1 : 2 ])

    accum = Y[0];
    accum += ( 2 * sum_1 )
    accum += ( 4 * sum_2 )
    accum += Y[-1];
    accum *= float( h / 3 )

    return accum

# count of X % 3 must be 0
def simpson_3_8( X , Y ):
    if (len(X)-1) % 3 : return None

    a = X[0]
    b = X[-1]
    n = len(X)-1
    h = float(b-a)/n

    sum_1 = sum(Y[ 1 : len(X)-1 : 3 ])
    sum_2 = sum(Y[ 2 : len(X)-1 : 3 ])
    sum_3 = sum(Y[ 3 : len(X)-1 : 3 ])

    accum = Y[0];
    accum += ( 3 * sum_1 )
    accum += ( 3 * sum_2 )
    accum += ( 2 * sum_3 )
    accum += Y[-1];
    accum *= float( 3 * h / 8 )

    return accum
