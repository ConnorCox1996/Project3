# Project3
==========
Schrodinger Equation 
===========




Overview
--------
The Schrodinger equation is one of the building blocks of quantum mechanics. This tool solves the Schrodinger Equation (in 1-D) using a Fourier basis set
By projecting the Hamiltonian operator into a particular basis set (the Fourier basis set) & evaluating the operator on a particular wavefunction,
the lowest-energy state of the Hamiltonian can be determined by solving for eigenvalues & eigenvectors of the matrix.


The Schrodinger equation is as follows:

     .. image:: https://latex.codecogs.com/gif.latex?%5Cinline%20%5Chat%7BH%7D%5CPsi%28x%29%20%3D%20E%5CPsi%28x%29

where H is the Hamiltonian operator, psi is the wavefunction, & E is the Energy


The Hamiltonian operator acting upon a particular wavefunction is as follows:

     .. image:: https://latex.codecogs.com/gif.latex?%5Cinline%20%5Chat%20H%20%5CPsi%28x%29%3D%20-c%5Cnabla%5E2%5CPsi%28x%29&plus;V_0%28x%29

where Vo is potential energy, c is a constant & del squared is the Laplacian


The Hamiltonian, as previously mentioned, is an operator which maps from L2 of complex functions to L2,
which allows computation of the inner-product on complex L2 according to the following:

     .. image:: https://latex.codecogs.com/gif.latex?%3Cf%28x%29%7Cg%28x%29%3E%20%5C%20%3D%5Cint%20%7Bf%28x%29%5Cbar%20%7Bg%28x%29%7D%20dx%7D
     
     where - represents the complex conjugate




Installation
-------------

Use the following command lines to install:


``git clone https://github.com/ConnorCox1996/Project3.git``


``cd Project3``




Usage
-------

Inputs:

* --size: 
        * Int, The size of the fourier basis set: {1, sin(x), cos(x), sin(2x), cos(2x)...}
        * default is 5

* --c:
        * Float, The constant in the Hamiltonian
        * default is 1

* --file:
        * String, The path and file name of the potential energy
        * optinal argument, default is schrodinger/potential_energy.dat
        * note: please begin the first line of the data file with "#" and the first column being position, second column being potential energy.
        * The position input has to be evenly distributed.

* --domain:
        * String, the domain of position
        * default is the domain of the input position data
        * note: please input the domain in the format of 'a,b' (seperate lower and upper bound by comma)
        * The domain input has to be within the range of position data
TODO
-------

* Revise the Hamiltonian
* Handle unevenly distributed position Inputs
