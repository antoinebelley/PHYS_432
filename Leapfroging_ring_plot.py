"""
Plottig code to plot 4 vortices representing the cross-section
of two rings of smoke (Question 6.2 "Leapfroging rings")

Author: Antoine Belley
Course : Phys 432
Instructor: Eve Lee

Date: 25/02/20
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Vortex import Vortex

#Initiate the grid
x = np.linspace(0,200, 100)
y = np.linspace(0,200, 100)
grid = np.meshgrid(x, y)

#Initiate the vortices and computes the total velocity field as t=0
v1 = Vortex(0.001, 100, grid, center=(1,80),velocity_CM=[3.0,0,0])
v3 = Vortex(0.001, 100, grid, center=(1,110),velocity_CM=[3.0,0,0], vorticity="down")
v2 = Vortex(0.001, 100, grid, center =(10,80))
v4 = Vortex(0.001, 100, grid, center =(10,110), vorticity="down")
velocity_x = v1.velocity_phi[0]+v2.velocity_phi[0]+v3.velocity_phi[0]+v4.velocity_phi[0]
velocity_y = v1.velocity_phi[1]+v2.velocity_phi[1]+v3.velocity_phi[1]+v4.velocity_phi[1]


#Creates figure and 
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("Velocity profile of the cross-section of Leapfroging rings")
ax.set_xlabel("X")
ax.set_ylabel("Y")

#Initiate the quiver and the plot of center of the vortices
vortices = ax.quiver(grid[0],grid[1], velocity_x,velocity_y)
center_1, = ax.plot(v1.center[0],v1.center[1],"ro")
center_2, = ax.plot(v2.center[0],v2.center[1],"bo")
center_3, = ax.plot(v3.center[0],v3.center[1],"ro")
center_4, = ax.plot(v4.center[0],v4.center[1],"bo")


#Function to stop the animation automatically when loop reaches the end when showing live
def gen():
    global center_1
    i = 0
    while v4.center[0]<= 200:
        i += 1
        yield i

#Update the plots at each step
def animate(i,quiver, X, Y):
    """perform animation step"""
    global v1,v2,v3,v4,center_1, center_2, center_3, center_4, ax, fig
    v1.update([v2,v3,v4])
    v2.update([v1,v3,v4])
    v3.update([v1,v2,v4])
    v4.update([v1,v2,v3])
    velocity_x = v1.velocity_phi[0]+v2.velocity_phi[0]+v3.velocity_phi[0]+v4.velocity_phi[0]
    velocity_y = v1.velocity_phi[1]+v2.velocity_phi[1]+v3.velocity_phi[1]+v4.velocity_phi[1]
    vortices.set_UVC(velocity_x, velocity_y)
    center_1.set_data([v1.center[0],v1.center[1]])
    center_2.set_data(v2.center[0],v2.center[1])
    center_3.set_data(v3.center[0],v3.center[1])
    center_4.set_data(v4.center[0],v4.center[1])
    return vortices, center_1, center_2, center_3, center_4


#Animate the plot
anim = animation.FuncAnimation(fig, animate,frames=300, fargs=(vortices, grid[0], grid[1]),
                               interval=50, blit=False, repeat=False)
fig.tight_layout()
#plt.show()
#Used to save the gif (Needs imagemagick installed)
anim.save('Leap_froging_rings.gif', writer='imagemagick')