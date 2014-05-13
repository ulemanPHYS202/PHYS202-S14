
import numpy as np
import matplotlib.pyplot as plt
def trapzz(func,x):
    """sums a set of trapezoids created from estimating the fxn then sums the trapezoids to estimate the integral"""
    a=0.0
    b=2.0
    h=(b-a)/x
    k = np.arange(1,x)
    I = h*(0.5*func(a) + 0.5*func(b) + func(a+k*h).sum())
    return I
   
def sims(func,x):
    """estimates the integral of a fxn by summing the area underneath quadratic curves estimated from 3 points on the fxn"""
    a = 0.0
    b = 2.0
    h = (b-a)/x

    k1 = np.arange(1,x/2+1)
    k2 = np.arange(1,x/2)
    I = (1./3.)*h*(func(a) + func(b) + 4.*func(a+(2*k1-1)*h).sum() + 2.*func(a+2*k2*h).sum())
    return I