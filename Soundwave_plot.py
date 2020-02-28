"""
Plottig code tp plot the time evolution of velocity and density
of a fluid into which a sound wave caused by a gaussian pertubation
is travelling.
Author: Antoine Belley
Course : Phys 432
Instructor: Eve Lee

Date: 25/02/20
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Hydro_solver import HydroSolver


#Initialize the insistance of the class  
fluid = HydroSolver(200)
#Apply the initial condition. Change the parameter to cahnge initial amplitude. 
fluid.Gaussian_ic(0.1)

#Creates figure and 
fig, ax = plt.subplots(1,2)
ax[0].set_xlim(-10,210)
ax[1].set_xlim(-10,210)
ax[0].set_title('Density of the fluid')
ax[1].set_title('Velocity of the fluid')
ax[0].set_ylim(0,5)
ax[1].set_ylim(-5,5)
ax0,= ax[0].plot(fluid.x,fluid.f1)
ax1, = ax[1].plot(fluid.x,fluid.f2/fluid.f1)



#Update the plots at each step
def animate(i):
    """perform animation step"""
    global fluid, ax0,ax1
    for i in range(20):
        fluid.update()
        ax0.set_data(fluid.x,fluid.f1)
        ax1.set_data(fluid.x,fluid.f2/fluid.f1)
    return ax0,ax1


#Animate the plot
anim = animation.FuncAnimation(fig, animate,frames=300,interval=50, blit=False, repeat=False)
fig.tight_layout()
plt.show()
#Used to save the gif (Needs imagemagick installed)
#anim.save('Sound_wave.gif', writer='imagemagick')