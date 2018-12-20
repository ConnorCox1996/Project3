Schrodinger Equation 
====================


Overview
--------
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
.. image:: https://latex.codecogs.com/gif.latex?%3Cf%28x%29%7Cg%28x%29%3E%20%5C%20%3D%5Cint%20%7Bf%28x%29%5Cbar%20%7Bg%28x%29%7D%20dx%7D
     
     where - represents the complex conjugate




Installation
-------------
-------------

The tool can be installed from the command line using:


``git clone https://github.com/ConnorCox1996/Project3.git``


``cd Project3``




Utilization
-----------
-----------

Inputs
-------
Inputs should be a table of values, with each entry in the table being a pair of position & potential energy values
Additional inputs are the size of the basis set, & a constant, 'c'

---IMPORTANT potential_energy.dat must be held in the same directory as Schrodinger.py & test_Schrodinger.py files--- 


Input Format
-------------


* position & potential energy -

     position & potential energy inputs should be entered into a comma-separated table
     The table should be saved as a .dat file with the filename potential_energy.dat

     The first entry of the table should read "Position,Potential Energy" followed underneath by the first position input, a comma, then    the first potential energy input

     Each additional set of position & energy values should be entered a line below previous entries
     *Please Note: "Position" & "Potential Energy" entries are case sensitive*

* c & basis set size -

     After all position & potential energy inputs are entered, the last entry in the .dat file should be the 'c' input, followed by a        comma, followed the 'size' input

     (in the example potential_energy.dat file, c=1 (bottom left entry) & size=7 (bottom right entry))

It is imporant that the last values in the .dat, reading left to right, are 'c', a comma, then 'size'
(where 'c' & 'size' are your desired inputs)


Example Input File
-------------------
For an example input file, see potential_energy.dat 

Running Program
---------------
---------------

To run the program from the command line, simply type 

``python Schrodinger.py``
 
Testing & Coverage
------------------
------------------

* Testing

To run unit tests for the Schrodinger.py tool from the command line type 

``python -m unittest test_Schrodinger.py``

* Coverage

To check program coverage from the command line type

``python -m coverage run Schrodinger.py``

``coverage report -m``

To-Do
-----
* Change algorithm for determining matrix eigenvalues & eigenvectors so that when basis set size & number of position and potential energy values aren't equal, eigenvalues & eigenvectors can still be computed

* Consider Edge cases with minimal basis set size

* Consider output when solving for eigenvalues & eigenvectors may produce infinite number of solutions
