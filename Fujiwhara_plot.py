"""
Plottig code to plot two vortices of same vorticity
interracting. (Question 6.2 "Fujiwhara effect")

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
x = np.linspace(0,10, 100)
y = np.linspace(0,10, 100)
grid = np.meshgrid(x, y)

#Initiate the vortices and computes the total velocity field as t=0
v1 = Vortex(0.001, 100, grid, center=(3,5))
v2 = Vortex(0.001, 100, grid, center =(6,5))

velocity_x = v1.velocity_phi[0]+v2.velocity_phi[0]
velocity_y = v1.velocity_phi[1]+v2.velocity_phi[1]


#Creates figure and 
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("Fujiwhara")
ax.set_xlabel("X")
ax.set_ylabel("Y")

#Initiate the quiver and the plot of center of the vortices
vortices = ax.quiver(grid[0],grid[1], velocity_x,velocity_y)
center_1, = ax.plot(v1.center[0],v1.center[1],"ro")
center_2, = ax.plot(v2.center[0],v2.center[1],"bo")

#Update the plots at each step
def animate(i,quiver, X, Y):
    """perform animation step"""
    global v1,v2,center_1, center_2, ax, fig
    v1.update([v2])
    v2.update([v1])
    velocity_x = v1.velocity_phi[0]+v2.velocity_phi[0]
    velocity_y = v1.velocity_phi[1]+v2.velocity_phi[1]
    vortices.set_UVC(velocity_x, velocity_y)
    center_1.set_data([v1.center[0],v1.center[1]])
    center_2.set_data(v2.center[0],v2.center[1])
    return vortices, center_1, center_2


#Animate the plot (will not stop until you close it.)
anim = animation.FuncAnimation(fig, animate,frames=200, fargs=(vortices, grid[0], grid[1]),
                               interval=50, blit=False, repeat=True)
fig.tight_layout()
plt.show()
#Used to save the gif (Needs imagemagick installed)
#anim.save('Fujiwhara.gif', writer='imagemagick')