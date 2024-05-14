import PDDOConstants
import numpy as np
from sklearn.neighbors import KDTree
from numpy.linalg import solve


class firstOrderDerivativePDDOKernel:
    def __init__(self):
        self.l1 = PDDOConstants.L1
        self.l2 = PDDOConstants.L2
        self.Nx = PDDOConstants.NX
        self.Ny = PDDOConstants.NY
        self.dx = self.l1/self.Nx
        self.dy = self.l2/self.Ny
        self.horizon = PDDOConstants.HORIZON1
        self.bVec10 = PDDOConstants.BVEC10
        self.bVec01 = PDDOConstants.BVEC01
        self.deltaX = self.horizon*self.dx
        self.deltaY = self.horizon*self.dy
        self.kernelDim = PDDOConstants.KERNELDIM1

    def createPDDOKernelMesh(self):
        indexing = 'xy'
        xCoords = np.arange(self.dx/2, (self.horizon*2 + 1)*self.dx, self.dx)
        yCoords = np.arange(self.dy/2, (self.horizon*2 + 1)*self.dy, self.dy)
        xCoords, yCoords = np.meshgrid(xCoords, yCoords, indexing=indexing)
        xCoords = xCoords.reshape(-1, 1)
        yCoords = yCoords.reshape(-1, 1)
        self.PDDOKernelMesh = np.array([xCoords[:,0], yCoords[:,0]]).T
    
    def calculateXis(self):
        midPDDONodeCoords = self.PDDOKernelMesh[int((len(self.PDDOKernelMesh)-1)/2),:]
        self.xXis = midPDDONodeCoords[0]-self.PDDOKernelMesh[:,0]
        self.yXis = midPDDONodeCoords[1]-self.PDDOKernelMesh[:,1]

    def calculateGPolynomials(self):
        deltaMag = np.sqrt(self.deltaX**2 + self.deltaY**2)
        diffMat = np.zeros([3,3])
        g10 = []
        g01 = []
        for iNode in range(len(self.PDDOKernelMesh)):
            currentXXi = self.xXis[iNode]
            currentYXi = self.yXis[iNode]
            xiMag = np.sqrt(currentXXi**2+currentYXi**2)
            pList = np.array([1, currentXXi/deltaMag, currentYXi/deltaMag])
            weight = np.exp(-4*(xiMag/deltaMag)**2)
            diffMat += weight*np.outer(pList,pList)*self.dx*self.dy
        for iNode in range(len(self.PDDOKernelMesh)):
            currentXXi = self.xXis[iNode]
            currentYXi = self.yXis[iNode]
            xiMag = np.sqrt(currentXXi**2+currentYXi**2)
            pList = np.array([1, currentXXi/deltaMag, currentYXi/deltaMag])
            weight = np.exp(-4*(xiMag/deltaMag)**2)
            g10.append((self.dx*self.dy/(np.sqrt(2)*self.horizon*self.dx))*weight*(np.inner(solve(diffMat,self.bVec10), pList)))
            g01.append((self.dx*self.dy/(np.sqrt(2)*self.horizon*self.dx))*weight*(np.inner(solve(diffMat,self.bVec01), pList)))
        
        self.g10 = np.array(g10).reshape((self.kernelDim,self.kernelDim))
        self.g01 = np.array(g01).reshape((self.kernelDim,self.kernelDim))
        self.g10[np.absolute(self.g10)<10**-9]=0
        self.g01[np.absolute(self.g01)<10**-9]=0
        self.gGradient = self.g10+self.g01
    
    def createPDDOKernels(self):
        self.calculateXis()
        self.calculateGPolynomials()

    def solve(self):
        self.createPDDOKernelMesh()
        self.createPDDOKernels()

