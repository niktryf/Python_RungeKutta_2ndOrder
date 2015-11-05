##############################################################################
### Python 2nd Order ODE solver, using the Runge-Kutta 4th order method
### Solves ordinary differential equations of the form 
###			
###			(d^2)x/(dt^2) = f(t, x, v)
###
### As usual, the 2nd order ODE is split into two coupled 1st order ODEs,
### which are solved with the Runge-Kutta function:
###
###                                     | x'(t) = v(t)
###              x''(t) = f(t, x, v) -> | 
###                                     | v'(t) = f(t, x, v)
###
### User must input the following parameters:
### 1. Via command line arguments: time step, total time, output interval.
### 2. The right-hand side of the differential equation 
###    inside the rhs function, in the rungekutta2.py file.
### 3. Initial conditions t_0, x_0, v_0 (example: x(t_0) = x_0, v(t_0) = v_0),
###    at the beginning of the code, right below the imports.
###
### The force can be specified inside the "force" function, in rungekutta2.py.
###
### Example: python ODE2.py 0.1 100 10
### This will solve the ODE with a timestep of dt = 0.1, for 100 time units,
### writing output every 10 time steps.
###
### Output: File "RK4_2_output.txt", also plots results.
### 
### Author: Nikos Tryfonidis, November 2015
### The MIT License (MIT)
### Copyright (c) 2015 Nikos Tryfonidis
### See LICENSE.txt
##############################################################################

# Import necessary packages
import numpy as np
import sys

# Import functions
from rungekutta2 import RK4_2nd
from plot1D import plot1D

##### Set Initial Conditions Here: #####
t_0 = 0.0
x_0 = 0.0
v_0 = 2.0
########################################

#################################################################################
### Command line arguments:
#################################################################################

# Check number of command line arguments
if len(sys.argv) != 4:
	print "Usage: python ODE2.py <timestep> <total time> <output interval>"
	print "Please run again following the command line input format above."
	print "Exiting..."
	sys.exit(1)

# Get command line arguments
h = float(sys.argv[1])
totalTime = float(sys.argv[2])
interval = int(sys.argv[3])

#################################################################################

# Calculate number of time steps
totalSteps = totalTime/h
# Find size of output
size = int(totalSteps/interval) + 1

# Print a summary of parameters
print "Running Runge-Kutta with the following parameters:"
print "Time step: %f\tTotal time: %f\t" %(h, totalTime)
print "Output interval: %d" %interval

# Allocate variable arrays and apply given initial conditions
t = np.linspace(t_0, t_0 + totalTime, size)

x = np.zeros(size)
x[0] = x_0

v = np.zeros(size)
v[0] = v_0

# Call Runge Kutta
tOld = t[0]
xOld = x[0]
vOld = v[0]
for i in xrange(1, size):
    for j in xrange(0, interval):
        tOld += h    # Unnecessary, but to keep generality
        xOld, vOld = RK4_2nd(tOld, xOld, vOld, h)        
    x[i] = xOld
    v[i] = vOld

# Save t, x and v into output file (each array is a column)
np.savetxt('RK4_2_output.txt', np.c_[t, x, v], fmt='%.10f')

# Plot t, x (plot1d function in plot1D.py)
plot1D(size, "RK4_2_output.txt")



