# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 18:16:17 2021

@author: laket
"""

import sys
import math

#Retrieves arguments from the command line provided by user.
#If user input is incorrect print usage information.
try:
    height = float(sys.argv[1])
    radius = float(sys.argv[2])
    area_or_volume = sys.argv[3]
    
except:
    print("Usage: \n$ python conegeomtry.py <height> " +
          "<radius> <area_or_volume>")
    sys.exit()

#initialize variables.    
area = 0
volume = 0

#Calculate area or volume depending on input.
#if input is invalid for area or volume print exception.
try:
    if area_or_volume == "area":
        area = math.pi * radius * (radius + math.sqrt(height**2 + radius**2))
        print("The surface area of a cone with radius: " + str(radius) + " and " +
              "height: " + str(height) + " is: " + str(area))
    elif area_or_volume == "volume":
        volume = math.pi * radius**2 * (height / 3)
        print("The volume of a cone with radius: " + str(radius) + " and " +
              "height: " + str(height) + " is: " + str(volume))
    else:
        raise Exception
except:
    print("\narea_or_volume: must be 'area' or 'volume'")