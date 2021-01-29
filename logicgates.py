# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 09:13:31 2021

@author: laket
"""

import ttg


#This is the boolean algebra for the expression in Fig. 2
q='((A and B)or(not C))and(D and E)'


#Using ttg print the input and output logic as a table.
print(ttg.Truths(['A', 'B', 'C','D','E'],[(q)]))
