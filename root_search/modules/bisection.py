import sympy as sym

x = sym.Symbol('x')

def zero( fx , a, b, tolerance):
    f = sym.lambdify(x, fx, "numpy")

    # initial condition, a...b must cross zero
    if f(a)*f(b) >= 0:
        return None;

    # find m within tolerance
    m = (a+b)/2.0
    while f(m) is not 0 and abs(f(b)-f(a)) > tolerance:
        m = (a+b)/2.0
        if f(a)*f(m) < 0:
            b = m;
        else:
            a = m;
    
    return m
