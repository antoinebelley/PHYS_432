# PHYS_432
My solution to problem set 4 of phys_432 given by Prof. Eve Lee on numerical analysis of fluid dynamics

* **Name**:    Antoine Belley
* **Version**: Phython 3.6 or higher (due to the use of "f-strings")

## Question 5
**Files**:
 * [Hydro-solver.py](https://github.com/antoinebelley/PHYS_432/blob/master/Hydro_solver.py): Contain a class describing the hydro solver. 
 * [Soundwave_plot.py](https://github.com/antoinebelley/PHYS_432/blob/master/Soundwave_plot.py): Plots the animation for a Gaussian perturbation causing sound wave in a fluid. Amplitude of the initial condition can be change by changing the parameter of the method Gaussian_ic() on line 22 of this file.
 
 **Answer to question asked in the problem set and results**:
 
As shown below we can see that for an initial amplitude of 4 for the Gaussian we do see a shock in the fluid. The the width of the shock wave is set by what is called a numerical viscosity which is induced by numerical error coming from the approximations done in the numerical methods. This iduces a artificial diffussion which explains that the amplitude of the perturbation is dissipating as time goes.

![Sound_wave.gif](https://github.com/antoinebelley/PHYS_432/blob/master/Sound_wave.gif)



## Question 6.2
**Files**:
  * [Vortex.py](https://github.com/antoinebelley/PHYS_432/blob/master/Vortex.py): Contains the class describing the vortices. Uses Numba to accelerate the computation of the velocity on the grid point. The package is in the Anaconda distribution but can be installed using pip if needed.
  * [Fujiwhara_plot.py](https://github.com/antoinebelley/PHYS_432/blob/master/Fujiwhara_plot.py): Plots the animation for the Fujiwhara effects using Vortex.py
  * [Paddle_plot.py](https://github.com/antoinebelley/PHYS_432/blob/master/Paddle_plot.py): Plots the animation for the "Paddle" effects using Vortex.py
  * [Leap_froging_rings_plot.py](https://github.com/antoinebelley/PHYS_432/blob/master/Leapfroging_ring_plot.py): Plots the cross-section of two smokes ring "Leapfrogging".
  
**Results**:
Results are showed below. Note that the scaling of the arrow is controlled by the quiver function, which causes the giant arrows and controlling this is quite messy so I decided no to...

![Fujiwhara.gif](https://github.com/antoinebelley/PHYS_432/blob/master/Fujiwhara.gif) 
![Paddle.gif](https://github.com/antoinebelley/PHYS_432/blob/master/Paddle.gif)  
![Leap_froging_rings_plot.gif](https://github.com/antoinebelley/PHYS_432/blob/master/Leap_froging_rings.gif)
