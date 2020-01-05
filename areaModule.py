# -*- coding: utf-8-*-

'''
Functions for calculating the training ground area:
- use the Gauss formula
- the input is a list of lists like: [[x, y], [x, y], ...]
- x and y - are coordinates of the polygon corners in 2D
- there are 2 functions:
	- area () - based on python language lists
	- araenp () - uses numpy arrays
'''

import numpy as np

# ---------------------------------------------------------------------

def area(coordinates):
    """ Describe what the function does and what arguments it accepts
    """
	#calculates the area using python lists
    return round(ssum,2)

# ---------------------------------------------------------------------

def areanp(coordinates):
    """ Describe what the function does and what arguments it accepts

    """
	# calculates the area using arrays of the numpy module
	# shifting arrays
    y1 = np.roll(y,1)	# yi - 1
    y2 = np.roll(y,-1)  # yi + 1

    # you have boards ready !!!
	# create a formula

    return .....



# ---------------------------------------------------------------------



