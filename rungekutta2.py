#############################################################################
### Runge-Kutta 4th Order 
###   for differential equations of the form (d^2)y/(dx^2) = (rhs) 
###   rhs: The right-hand side function of the ODE.
###   Newton's 2nd Law formalism has been kept (rhs = f(t, x, v)/m)
###
###  
###   Author: Nikos Tryfonidis
###   The MIT License (MIT)
###   Copyright (c) 2015 Nikos Tryfonidis
###   See LICENSE.txt
#############################################################################

#############################################################################
### Force Function: Enter desired force function here.
### Form: f(t, x, v) = m*t + k*x + l*v
#############################################################################
def force(t, x, v):
    m = 1.0 #t coefficient
    k = 1.0 #x coefficient
    l = 0.01 #v coefficient
    return -k*x -l*v

#############################################################################

#############################################################################
# Right-hand side function of the 2nd order ODE. 
# This version sticks to Newton's 2nd law formalism
# (x''(t) = Force/mass)
#############################################################################
def rhs(t, x, v):
    mass = 1.0
    return force(t, x, v)/mass

#############################################################################

# Function for the x'(t) = v ODE.
def g(v):
    return v

# Runge - Kutta 4th Order Method, for 2nd Order ODEs:
def RK4_2nd(t, x, v, h):
        
    k0 = h*g(v)
    l0 = h*rhs(t, x, v)

    k1 = h*g(v + 0.5*l0)
    l1 = h*rhs(t + 0.5*h, x + 0.5*k0, v + 0.5*l0)

    k2 = h*g(v + 0.5*l1)
    l2 = h*rhs(t + 0.5*h, x + 0.5*k1, v + 0.5*l1)

    k3 = h*g(v + l2)
    l3 = h*rhs(t + h, x + k2, v + l2)

    x_new = x + (1.0/6.0)*(k0 + 2*(k1+k2) +k3)
    v_new = v + (1.0/6.0)*(l0 + 2*(l1+l2) +l3)

    return (x_new, v_new)

