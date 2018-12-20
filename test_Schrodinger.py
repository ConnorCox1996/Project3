import Schrodinger
import unittest
import math
import numpy as np 
import tensorflow as tf 
tf.enable_eager_execution()
#include test for what happens if basis set has Ex: 1 or 0 size
##### ----->    WRITE COMMENTS EXPLAINING TESTS?????

testPositions=[0.0, 1.57079, 3.14159, 4.71238, 6.28318, 7.85398, 9.42477]
testEnergies=[0.0, 6.0, 0.0, -6.0, 0.0, 6.0, 0.0]


class TestDeltaSquareFunc(unittest.TestCase):
    def test_deltaSquareFunc(self):
        set1=Schrodinger.deltaSquareFunc(3)
        set2=Schrodinger.deltaSquareFunc(7)
        set3=Schrodinger.deltaSquareFunc(10) 
        aVals1=set1[0]
        aVals2=set2[0]
        aVals3=set3[0]
        set1Fns=set1[1]
        set2Fns=set2[1]
        set3Fns=set3[1]

        #Check length for various basis size inputs
        l11=len(set1[0])
        l12=len(set1[1])
        l21=len(set2[0])
        l22=len(set2[1])
        l31=len(set3[0])
        l32=len(set3[1])
        self.assertEqual(l11,3)
        self.assertEqual(l12,3)
        self.assertEqual(l21,7)
        self.assertEqual(l22,7)
        self.assertEqual(l31,10)
        self.assertEqual(l32,10)

        #Check first element of each set (after taking del**2)
        #Should always=0, regardless of specified size
        set1a1=aVals1[0]
        set2a1=aVals2[0]
        set3a1=aVals3[0]
        self.assertEqual(set1a1,0)
        self.assertEqual(set2a1,0)
        self.assertEqual(set3a1,0)
        
        #Check last element of each set (after taking del**2) for various basis set size inputs
        set1aLast=aVals1[-1]
        set2aLast=aVals2[-1]
        set3aLast=aVals3[-1]
        self.assertEqual(set1aLast,1)
        self.assertEqual(set2aLast,3)
        self.assertEqual(set3aLast,5)
        
        #check evaluation of functions, for various basis set size inputs
        set1LastFn=set1Fns[-1]
        set2LastFn=set2Fns[-1]
        set3LastFn=set3Fns[-1]
        eval1=set1LastFn(set1aLast,0)
        eval2=set2LastFn(set2aLast,math.pi/3)
        eval3=set3LastFn(set3aLast,math.pi/10)
        self.assertEqual(eval1,-1)
        self.assertEqual(eval2,9)
        self.assertEqual(eval3,-25)

class TestOperatorMatrix(unittest.TestCase):
    def test_operatorMatrix(self):
        one=[0,1,2,3]
        two=[2.65e-06,1,2,3]
        np.testing.assert_allclose(one, two, rtol=1e-6, atol=1e-5)
        pos=testPositions
        potE=testEnergies

        #BASIS SET SIZE = 3 Check equivalence of each matrix column 
        #(check correctness of operator represented in matrix form)
        sets=Schrodinger.deltaSquareFunc(3)
        setYs=sets[0]
        setDels=sets[1]        
        mat=Schrodinger.operatorMatrix(pos, potE, setYs, setDels,1)
        matCol1=mat[0][:,0]
        
        matCol2=mat[0][:,1]
        matCol3=mat[0][:,2]
        
        first=[0,6,0,-6,0,6,0]
        second=[0,7,0,-7,0,7,0]
        third=[1,6,-1,-6,1,6,-1]
        testMat=[]
        testMat.append(first)
        testMat.append(second)
        testMat.append(third)

        np.testing.assert_allclose(matCol1,first, rtol=1e-6, atol=0)
        np.testing.assert_allclose(matCol2,second, rtol=1e-6, atol=1e-4)
        np.testing.assert_allclose(matCol3,third, rtol=1e-6, atol=1e-5)


class TestGenerateTfMatrix(unittest.TestCase):
    def test_generateTfMatrix(self):
       testSet=Schrodinger.deltaSquareFunc(3)
       yValues=testSet[0]
       deltas=testSet[1]
       numpMat=Schrodinger.operatorMatrix(testPositions, testEnergies,yValues,deltas,1)
       tfMat=Schrodinger.generateTfMatrix(numpMat)
       shape=tfMat.get_shape().as_list()
       self.assertEqual(shape, [7,3])

       matrixType=tfMat.dtype
       self.assertEqual(matrixType, tf.float64)

class TestEigen(unittest.TestCase):
    def test_Eigen(self):
        eigPositions= [0.0, 1.57079, 3.14159]
        eigEnergies= [0.0, 6.0, 0.0]
        testSet=Schrodinger.deltaSquareFunc(3)
        yValues=testSet[0]
        deltas=testSet[1]
        numpMat=Schrodinger.operatorMatrix(eigPositions, eigEnergies, yValues, deltas,1)
        tfMat=Schrodinger.generateTfMatrix(numpMat)

        e,v=Schrodinger.eigen(tfMat)
        valueShape=e.get_shape().as_list()
        valueType=e.dtype
        self.assertEqual(valueShape, [3])
        self.assertEqual(valueType, tf.float64)
        vectorShape=v.get_shape().as_list()
        vectorType=v.dtype
        self.assertEqual(vectorShape, [3,3])
        self.assertEqual(vectorType, tf.float64)


        

if __name__== '__main__':
    unittest.main()
        