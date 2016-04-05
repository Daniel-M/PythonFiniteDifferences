# PythonFiniteDifferences

# Description
I needed to debug some Finite Difference Routines associated to 2D cylindrical coordinates finite differences
in the time domain for the Diffusion problem.  
Individual 1D and 2D cases where considered,

* 1D considers the case for diffusion along the `r` coordinate and `z` coordinate independently (source code for each case),
  the time evolution is Fordward Euler.   
* 2D considers both coordinates (the same algorithms for 1D case but combined since FD operators are linear) and evolves time in a Euler-forward fashion.  

The initial condition is *always* a Gaussian curve/surface with the maximum located at the center of the domain.  
