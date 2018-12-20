
import tensorflow as tf 
tf.enable_eager_execution()
from tensorflow import linalg
import math
import numpy as np

''' Handling Input Table
------------------------------------------------------------------
    Reads position, potential energy, c, & basis set size values from input table,
    table should be a .dat file saved as 
    "potential_energy.dat"
    the table should appear as follows: "Positions, Potential Energy"
    *Note these values are comma separated*
    position & potential energy values should be include pairwise, separated by commas (one position & one potential energy value per line)
    
    Values will be converted to floating point numbers

    OTHER INPUTS: the LAST ROW OF THE TABLE should include c & basis set size values
    in the order "c, size"

**Please Note: these values will be printed to the console to ensure they have been read as expected**

.................................................................
-->position & potential energy Table must be saved in the same directory this Schrodinger.py file is saved to & run from
.................................................................

Position & Potential Energy Values are stored in 'positions' & 'potentialEnergy' arrays
to make values accessible for calculations
'''

import csv
with open('potential_energy.dat', 'r') as file:
    reader = csv.DictReader(file)
    positions=[]
    potentialEnergy=[]

    for row in reader:
        positions.append(float(row['Position']))
        potentialEnergy.append(float(row['Potential Energy']))
c=positions[-1]
positions.pop(-1)
size=potentialEnergy[-1]
potentialEnergy.pop(-1)

print('Position array ')
print(positions)
print('')
print('Potential Energy array')
print(potentialEnergy)
print('')
print('c')
print(c)
print('')
print('size')
print(size)



''' deltaSquareFunc
 -------------------------------------------------------------------------------------------------
    function computes del**2 of each element in the basis set
    where the basis set is the Fourier series of n # of terms, where n is the specified basis size
 -------------------------------------------------------------------------------------------------
Please Note: Complications with handling lambda functions generated via iteration
               have caused unusual form of these values (components of values stored amongst 2 arrays) 

**The fourier series is written as follows:
    = a0 + [summation(from 0 to N) aNsin(aN)] + [summation(from 0 to M) aMcos(aM)]
** del**2 of each term (exclusive of the first, where del**2 of term =0) is written as follows:
    = [summation(from 0 to N) -(aN**2)*sin(aN)] + [summation from(0 to M) -(aM**2)*cos(aM)]


INPUT-->size of basis set
RETURNS--> 2 arrays, Array 1: a list of aN & aM terms (see above)
                     Array 2: lambda functions which take x & y inputs, where y is an aN or aM value, & x is the value which the function is evaluated at 

'''
def deltaSquareFunc(size):
    delt=[lambda y,x: 0]
    yValues=[0]
    terms=math.ceil( (size-1)/2)

    for i in range(1,terms+1):
        yValues.append(i)
        yValues.append(i)
    if (len(yValues)>size):
        yValues.pop(-1)

    for i in range(1,terms+1):
        delt.append(lambda y,x: -(y**2)*math.sin(y*x))
        delt.append(lambda y,x: -(y**2)*math.cos(y*x))
    if(len(delt)>size):
        delt.pop(-1)   

    return yValues, delt
   


''' operatorMatrix
------------------------------------------------------------------------------------------------------------------------------
    Hhat(psi(x))=-c*del**2(psi(x))+Vo(x)
    this function maps Hhat to a matrix, representing the operator
------------------------------------------------------------------------------------------------------------------------------    
    Function takes del**2 values previously calculated for each element of the basis set,
    For each pair of Position & Potential Energy values provided, the Hamiltonian is evaluated by numerical integration
    Application of the operator to each element of the basis set, at each pair of values is mapped to a matrix, 
    which is used to represent the Schrodinger Equation in our basis set

INPUTS --> array of Position values, array of Potential Energy values, the arrays representing the basis set, & constant "c"
OUTPUTS--> a numpy matrix representing the operator, & the dimensions of the matrix
'''

def operatorMatrix (positions, potentialEnergy, yValues, deltaList,c):
    matrix = np.zeros((len(positions), len(deltaList)))

    for i in range(0,len(yValues)):
        # Ham.append('NEW')
        del2=deltaList[i]
        for j in range(0, len(positions)):
            opEval = (-c*del2(yValues[i],positions[j]))+potentialEnergy[j]
            matrix[j][i]=opEval
            dim=[len(deltaList),len(positions)]
    return matrix,dim

#evaluating del**2 of each basis set element
source=deltaSquareFunc(size)
ys=source[0]
fns=source[1]
#generating the numpy matrix representing the operator
first = operatorMatrix(positions, potentialEnergy, ys, fns,c)

''' generateTfMatrix
---------------------------------------------------------------------------------------------------------------------
    Tensorflow is used to solve the eigenvalue eigenvector problem which allows the determination of the wavefunction
    to do this, the operator matrix must be represented as a tensor (a tensorflow matrix, w/ particular shape)
    this function converts the numpy matrix to a matrix tensorflow tensor
---------------------------------------------------------------------------------------------------------------------
INPUTS --> Numpy Matrix
OUTPUTS--> Matrix form Tensorflow tensor (usable with tf.linalg.eigh())   
'''
def generateTfMatrix(Matrix):
    matr=Matrix[0]
    col=Matrix[1][0]
    rows=Matrix[1][1]

    hold=[]
    for i in range(0,rows):
        row=matr[i,:]
        hold.extend(row)

    tens=tf.Variable(tf.zeros(col*rows))
    tens=tf.assign(tens,hold)
    tens=tf.reshape(tens,[rows,col])
    tens=tf.cast(tens, tf.float64)
    return tens

#generate tf matrix
matrixgen=generateTfMatrix(first)

''' eigen
    ----------------------------------------------------------------------------------------
    by computing the eigen values and eigen vectors corresponding to the operator matrix,
    an eigenvalue corresponding to the lowest energy wave function can be computed,
    and the eigenvectors corresponding to that eigenvalue represent the coefficients of the
    lowest energy wavefunction
    for a particular basis set, representing the schrodinger equation in 1D
    -----------------------------------------------------------------------------------------
INPUTS --> Matrix form tensorflow tensor
OUTPUTS--> eigenvalue & eigenvector corresponding to the lowest enegy wavefunction for the inputs given
'''
def eigen(tensorMatrix):
    e,v=tf.linalg.eigh(tensorMatrix)
    eigenValue=e[0]
    print('Lowest Energy State of Hamiltonian : ')
    print(e[0])
    print('')
    print('Basis Set Coefficients for wavefunction correspondin to lowest-energy state')
    print(v[0])
    return e,v

tfm=generateTfMatrix(first)
res=eigen(tfm)
#print(res)
