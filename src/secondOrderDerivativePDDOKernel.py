import PDDOConstants
import numpy as np
from sklearn.neighbors import KDTree
from numpy.linalg import solve


class secondOrderDerivativePDDOKernel:
    def __init__(self):
        self.l1 = PDDOConstants.L1
        self.l2 = PDDOConstants.L2
        self.Nx = PDDOConstants.NX
        self.Ny = PDDOConstants.NY
        self.dx = self.l1/self.Nx
        self.dy = self.l2/self.Ny
        self.horizon = PDDOConstants.HORIZON2
        self.bVec20 = PDDOConstants.BVEC20
        self.bVec02 = PDDOConstants.BVEC02
        self.deltaX = self.horizon*self.dx
        self.deltaY = self.horizon*self.dy
        self.kernelDim = PDDOConstants.KERNELDIM2

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
        diffMat = np.zeros([6,6])
        g20 = []
        g02 = []
        for iNode in range(len(self.PDDOKernelMesh)):
            currentXXi = self.xXis[iNode]
            currentYXi = self.yXis[iNode]
            xiMag = np.sqrt(currentXXi**2+currentYXi**2)
            pList = np.array([1, currentXXi/deltaMag, currentYXi/deltaMag, (currentXXi/deltaMag)**2, \
                    (currentYXi/deltaMag)**2, (currentXXi/deltaMag)*(currentYXi/deltaMag)])
            weight = np.exp(-4*(xiMag/deltaMag)**2)
            diffMat += weight*np.outer(pList,pList)*self.dx*self.dy
        for iNode in range(len(self.PDDOKernelMesh)):
            currentXXi = self.xXis[iNode]
            currentYXi = self.yXis[iNode]
            xiMag = np.sqrt(currentXXi**2+currentYXi**2)
            pList = np.array([1, currentXXi/deltaMag, currentYXi/deltaMag, (currentXXi/deltaMag)**2, \
                    (currentYXi/deltaMag)**2, (currentXXi/deltaMag)*(currentYXi/deltaMag)])
            weight = np.exp(-4*(xiMag/deltaMag)**2)
            g20.append((self.dx*self.dy/(self.horizon**2*self.dx**2))*weight*(np.inner(solve(diffMat,self.bVec20), pList)))
            g02.append((self.dx*self.dy/(self.horizon**2*self.dy**2))*weight*(np.inner(solve(diffMat,self.bVec02), pList)))
        
        self.g20 = np.array(g20).reshape((self.kernelDim,self.kernelDim))
        self.g02 = np.array(g02).reshape((self.kernelDim,self.kernelDim))
    
    def createPDDOKernels(self):
        self.calculateXis()
        self.calculateGPolynomials()

    def solve(self):
        self.createPDDOKernelMesh()
        self.createPDDOKernels()

