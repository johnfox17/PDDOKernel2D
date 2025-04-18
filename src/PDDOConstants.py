import numpy as np
#Defining constants for PDDO algorithm
L1 = 1
L2 = 1
NX = 512
NY = 512
HORIZON0 = 1.015
HORIZON1 = 2.015
HORIZON2 = 3.015
HORIZON4 = 5.015 #Because the PDE is 4th order
BVEC00 = np.array([1])
BVEC10 = np.array([0, 1, 0])
BVEC01 = np.array([0, 0, 1])
BVEC11 = np.array([0, 0, 0, 1]) 
BVEC20 = np.array([0, 0, 0, 2, 0, 0])
BVEC02 = np.array([0, 0, 0, 0, 2, 0])
BVEC40 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 0, 0, 0, 0])
BVEC04 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 0, 0, 0])
KERNELDIM0 = 3
KERNELDIM1 = 5
KERNELDIM2 = 7
KERNELDIM4 = 11
A = 1
B = 1
N = 2
M = 2

