# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 09:58:23 2021

@author: laket
"""

import sys

#Retrieves arguments from the command line provided by user.
#If user input is incorrect print usage information.
try:
    m_dimension = int(sys.argv[1])
    n_dimension = int(sys.argv[2])
    p_dimension = int(sys.argv[3])
    
except:
    print("Usage: \n$ python matrixmultiplication.py <m_dimension> " +
          "<n_dimension> <p_dimension>")
    sys.exit()

#Setup for Matrix A
A = []
for ii in range(0, m_dimension):
    # In each iteration, add an empty list to the main list.
    A.append([])
    
print("Enter Values for Matrix A:")
for jj in range(0, m_dimension): #Fill Matrix A with values.
    for kk in range(0, n_dimension):
        print("Enter element A[" + str(jj) + "]["+ str(kk) + "]")
        A[jj].append(input())
        
#Setup for Matrix B
B = []
for mm in range(0, n_dimension):
    # In each iteration, add an empty list to the main list
    B.append([])

print("Enter Values for Matrix B:")
for nn in range(0, n_dimension): #Fill Matrix B with values.
    for oo in range(0, m_dimension):
        print("Enter element B[" + str(nn) + "]["+ str(oo) + "]")
        B[nn].append(input())
     
        
#Initialize Matrix C
C = []
sum=0
for pp in range(0, p_dimension):
    # In each iteration, add an empty list to the main list.
    C.append([])
    

#Element by element multiplication of A and B
for zz in range(0, p_dimension): #Cycle through the rows in C.
    for qq in range(0, p_dimension): #Append element results to the row.
        for rr in range(0, n_dimension): #Perform summing of element products.
            sum+=int(A[qq][rr])*int(B[rr][zz])
        C[qq].append(sum)
        sum = 0

#Display things nicely in a matrix-type format.       
print("The matrix product C is: ")
for yy in range (0, p_dimension):
    print(C[yy])

        
        
        
        
        
        
        
        