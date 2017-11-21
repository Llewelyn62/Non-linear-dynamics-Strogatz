# make a cobweb plot
import numpy as np
#from numpy import cos
import matplotlib.pyplot as plt

# here is the function we want to iterate
# mu is a possible parameter
def func(x,mu):
	return mu*np.sin(x*(1.0*np.pi)) #mu*x*(1-x)

# return f^n(x)
def func_n(x,mu,n):
	for i in range(0,n):
		x = func(x,mu)

	return x
# here is "plotting graphical" or "cobweb" for an interated map
# connect up (x, f^1(x)), (f^1(x),f^1(x)), (f^1(x), f^2(x)), (f^2(x),f^2(x))
#  ... (f^i(x), f^(i+1)(x)),(f^(i+1),f^(i+1)) to i=n
# initial x0, mu is a parameter to pass to function
# connect up points n times, this is 2n pairs of points
def plot_graphical(x0,mu,n):
	xv = np.linspace(0.0,1.0,2*n)  # create array for points xvalue 
	yv = np.linspace(0.0,1.0,2*n)  # create array for points yvalue 
	x =x0
	for i in range(0,n):  #iterate
		xv[2*i] = x  # first point is (x,f(x))
		x = func(x,mu)
		yv[2*i] = x
		xv[2*i+1] = x #second point is (f(x),f(x))
		yv[2*i+1] = x
	plt.plot(xv,yv,'b')  # connect up all these points blue

plt.figure()
plt.xlabel('x')
plt.ylabel('f(x)')
fac=1.01
xmax = 1.00
xmin =-0.01
ymax = 1.01
ymin =-0.01
plt.axis([xmin*fac,xmax*fac,ymin*fac,ymax*fac])
xcon = np.arange(xmin, xmax, 0.01)   # to plot function 
plt.plot(xcon,xcon, 'g')             #y=x plotted gree

mu=.3
ycon = func(xcon,mu)                 # function computed
plt.plot(xcon,ycon, 'r')             # function plotted red
plot_graphical(0.3,mu,50)            # cobweb plot, 0.3 is initial condition
plt.show()
#X, Y =plot_graphical(0.3,mu,5)
