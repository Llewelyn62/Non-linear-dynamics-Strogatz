from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from mayavi import mlab

#Torus
#+++++++++++++++++++++++++++++++++
#http://goanna.cs.rmit.edu.au/~gl/teaching/cosc1226/notes/parametric.pdf
#https://pritschet.me/wiki/python/example-scripts-python/plotting-complicated-surfaces-mayavi/
#x = (R + rcos(v))cos(u)
#y = (R + rcos(v))sin(u)
#z= -rsin(v)
p,q = 5,1
mlab.figure(size=(900,800), bgcolor=(0,0,0), fgcolor=(1,1,1))
#Plots a meshplane
# r, v = np.mgrid[.5:.6:200j, -p*np.pi:p*np.pi:200j] #Cross section
# R, u = np.mgrid[1:1.1:200j, -q*np.pi:q*np.pi:200j] #Torus big circle
#mobj = mlab.mesh(x,y,z)

r = np.linspace(.5,.6,200)
R = np.linspace(1,1.1,200)
v = np.linspace(-p*np.pi,p*np.pi,200)
u = np.linspace(-q*np.pi,q*np.pi,200)

#Create coordinates
x = (R + r*np.cos(v))*np.cos(u)
y = (R + r*np.cos(v))*np.sin(u)
z= -r*np.sin(v)
#Plot a string around the torus. 
mobj = mlab.plot3d(x,y,z, z, colormap='jet')
mlab.orientation_axes(xlabel='x',ylabel='y',zlabel='z')
#mlab.outline(opacity=.1)
#Shadow torus
s = mlab.pipeline.parametric_surface()
s.function = 'torus'
mlab.pipeline.surface(s,
                                color=(1,1,1),
                                opacity=.1,
                                representation='wireframe')
plt.show()
# @mlab.animate
# def anim(delay=200):
#     f = mlab.gcf()
#     while 1:
#         f.scene.camera.azimuth(20)
#         f.scene.render()
#         yield
# 
# a = anim() # Starts the animation.
