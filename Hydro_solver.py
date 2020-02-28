"""
Hydro Solver for sound wave caused by 
1D gaussian pertubation. This corresponds to question 5 
in the problem set.

Author: Antoine Belley
Course : Phys 432
Instructor: Eve Lee

Date: 26/02/20
"""
import numpy as np
from matplotlib import pyplot as plt

def Gaussian(x,u,A):
    """Gaussian function for the density.
    -Attributes: -x (array): x-coord where to evaluate the gaussian
                 -u (float): Mean of the gaussian
                 -A (float): Amplitude of the gaussian

    -Return: Gaussian (array): The value of the gaussian evaluated at the x-point"""
    return A*np.exp(-((x-u)/5)**2)


class HydroSolver():
    """Class to find the solution of the fluid density and velocity for a
    sound wave in a fluid caused by a Gaussian distributuion.

    -Methods:*__init__()          : Initialize the instance of the hydro solver and initialize the attributes.
             *Gaussian_ic(A)      : Set up the initial condition for the fluid.
             *boundary_condition(): Applies the boundary conditions to solve the PDE. Note
                                    that the indexing is different than the one give by Professor Lee since
                                    I defined my J1 and J2 a bit differenlty for the indices but the two are equivalent.
            *get_velocity()       : Find the velocity of the fluid at each time step.
            *J()                  : Computes the gradient of a given quantity
            *update()             : Updates the fluid for a timestep. First call the method get_velocity() to compute the velocity of the fluid.
                                    Then computes the J1 and J2 using the method method J(). With J1 and J2, update the values of f1 and f2 and finally
                                    calls the method boundary_condition() in order to apply the bc's.

    -Attributes:*dt       (float): The time step to take when updating the fluids
                *dx       (float): Space between ecah grid point
                *range      (int): Range in which we place the fluid
                *size       (int): The number of point in the grid
                *x        (array): Array containing the x points. Use to generate the IC and plotting
                *f1       (array): Array containing the values of f1=rho at each grid point
                *f2       (array): Array containing the values of f2=velocit*rho at each grid point
                *velocity (array): Velocity at the boundary ogf each grid cell
                *J1       (array): The gradient of f1=rho  between the cells
                *J2       (array): The gradient of f2=rho*u"""

    def __init__(self,size,dx=1, dt= 0.1):
        """Initialize the class attributes. 

        -Arguments: *self (HydroSolver object): The instance of the class
                    *size                (int): The x-range in which the fluid is.
                    *dx                (float): The x-step for the solver
                    *dt                (float): The time step of the solver

        -Retrun: None"""
        self.dt = dt
        self.dx=dx
        self.range = size
        self.size = int(size/dx)
        self.x = np.linspace(0,size,self.size)
        self.f1 = np.zeros(self.size)
        self.f2 = np.zeros(self.size)
        self.velocity = np.zeros(self.size-1)
        self.J1 = np.zeros(self.size-2)
        self.J2 = np.zeros(self.size-2)

    def Gaussian_ic(self,A):
        """Set up the initial condition for the fluid.
        -Arguments: *self (HydroSolver object): The instance of the class
                    *A                 (float): Desired amplitude of the gaussian

        -Return: None
        """
        self.f1 = Gaussian(self.x,self.range//2,A)+0.1

    def boundary_condition(self):
        """Applies the boundary conditions to solve the PDE. Note
        that the indexing is different than the one give by Professor Lee since
        I defined my J1 and J2 a bit differenlty for the indices but the two are equivalent.
        -Arguments: *self (HydroSolver object): The instance of the class

        -Returns: None """
        self.f1[1] = self.f1[1] - self.dt/self.dx * self.J1[2] 
        self.f1[-2] = self.f1[-2] + self.dt/self.dx * self.J1[-3]
        self.f2[1] = self.f2[1] - self.dt/self.dx * self.J2[0] 
        self.f2[-2] = self.f2[-2] + self.dt/self.dx * self.J2[-3]

    def get_velocity(self):
        """Find the velocity of the fluid at each time step.
        -Arguments: *self (HydroSolver object): The instance of the class

        -Returns: None """
        self.velocity = 0.5*(self.f2[:-1]/self.f1[:-1]+self.f2[1:]/self.f1[1:])

    def J(self,f):
        """Coputes the gradient of a certain qauntity. Those are referred as J1 for f1 and J2 for f2 
        in the notes.
        -Arguments: *self (HydroSolver object): The instance of the class
                    *f                 (array): The quantity that we desired to compute the gradient of.

        -Returns: None """
        J_plus = np.zeros(self.size-2)
        J_minus = np.zeros(self.size-2)
        v_plus = self.velocity[1:]
        v_positive=v_plus>0
        J_plus[v_positive] = f[1:-1][v_positive]*v_plus[v_positive]
        v_negative=self.velocity[1:]<=0
        J_plus[v_negative] += f[2:][v_negative]*v_plus[v_negative]
        v_minus = self.velocity[:-1]
        v_positive=v_minus>0
        J_minus[v_positive] = f[:-2][v_positive]*v_minus[v_positive]
        v_negative=v_minus<=0
        J_minus[v_negative] += f[1:-1][v_negative]*v_minus[v_negative]
        return J_plus - J_minus

    def update(self):
        """Update the fluids for one time step.
        -Arguments: *self (HydroSolver object): The instance of the class

        -Returns: None """
        self.get_velocity()
        self.J1 = self.J(self.f1)
        self.f1[1:-1] -= self.J1*self.dt/self.dx
        self.J2 = self.J(self.f2) + self.dt/self.dx*(self.f1[2:]-self.f1[:-2])
        self.f2[1:-1] -= self.J2*self.dt/self.dx
        self.boundary_condition()




# #Initialize the insistance of the class  
# fluid = HydroSolver(200)
# #Apply the initial condition
# fluid.Gaussian_ic(4)

# #Set up the plotting figure
# plt.ion()
# fig, ax = plt.subplots(1,2)
# ax[0].set_xlim(-10,210)
# ax[1].set_xlim(-10,210)
# ax[0].set_title('Density of the fluid')
# ax[1].set_title('Velocity of the fluid')
# ax[0].set_ylim(0,5)
# ax[1].set_ylim(-5,5)
# ax0,= ax[0].plot(fluid.x,fluid.f1)
# ax1, = ax[1].plot(fluid.x,fluid.f2/fluid.f1)

# #Loop to update the sound wave
# for i in range(3000):
#         fluid.update()
#         ax0.set_data(fluid.x,fluid.f1)
#         ax1.set_data(fluid.x,fluid.f2/fluid.f1)
#         plt.pause(1e-3)