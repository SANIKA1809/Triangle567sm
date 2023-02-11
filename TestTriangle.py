# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangler import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    
    # define multiple sets of tests as functions with names that begin

     # Testing Scalene Triangles
     def testScaleneTriangle1(self):
        self.assertEqual(classify_triangle(5,7,1), 'Scalene')

     def testScaleneTriangle2(self):
         self.assertEqual(classify_triangle(10,3,5), 'Scalene') 
    
    # Testing Right Triangles
     def testRightTriangle1(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right')

     def testRightTriangle2(self):
        self.assertEqual(classify_triangle(5, 3, 4), 'Right')

    
     def testEquilateralTriangle1(self):
            self.assertEqual(classify_triangle(1,1,1), 'Equilateral')

     def testEquilateralTriangle2(self):
        self.assertEqual(classify_triangle(3,3,3), 'Equilateral')

    

    # Testing Isosceles Triangles
     def testIsoscelesTriangle1(self):
        self.assertEqual(classify_triangle(5, 5, 1), 'Isosceles')

     def testIsoscelesTriangle2(self):
        self.assertEqual(classify_triangle(5, 1, 5), 'Isosceles')

     def testIsoscelesTriangle3(self):
        self.assertEqual(classify_triangle(1, 5, 5), 'Isosceles')

   

   

    # Testing Invalid Inputs
     def testInvalidInput1(self):
        self.assertEqual(classify_triangle(1,3,5), 'InvalidInput')

     def testInvalidInput3(self):
        self.assertEqual(classify_triangle(1,4,5), 'InvalidInput')
    

    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

