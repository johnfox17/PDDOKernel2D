import PDDOConstants
import numpy as np
from sklearn.neighbors import KDTree

class create2DSignals:
    def __init__(self):
        self.l1 = PDDOConstants.L1
        self.l2 = PDDOConstants.L2
        self.Nx = PDDOConstants.NX
        self.Ny = PDDOConstants.NY
        self.dx = self.l1/self.Nx
        self.dy = self.l2/self.Ny
        self.A = PDDOConstants.A
        self.B = PDDOConstants.B
        self.N = PDDOConstants.N
        self.M = PDDOConstants.M

    def createCoordinates(self):
        indexing = 'xy'
        xCoords = np.arange(self.dx/2, self.l1, self.dx)
        yCoords = np.arange(self.dy/2, self.l2, self.dy)
        xCoords, yCoords = np.meshgrid(xCoords, yCoords, indexing=indexing)
        xCoords = xCoords.reshape(-1, 1)
        yCoords = yCoords.reshape(-1, 1)
        self.PDDOCoordinateMesh = np.array([xCoords[:,0], yCoords[:,0]]).T
    
    def createSurface(self):
        self.surface = np.zeros(self.Nx*self.Ny)
        for iCoord in range(self.Nx*self.Ny):
            self.surface[iCoord] = self.A*self.PDDOCoordinateMesh[iCoord,0]**self.M*self.B*self.PDDOCoordinateMesh[iCoord,1]**self.N
        self.surface = self.surface.reshape((self.Nx,self.Ny))
    
    def calculateAnalyticalXDerivativeOfSurface(self):
        self.analyticalXDerivativeOfSurface = np.zeros(self.Nx*self.Ny)
        for iCoord in range(self.Nx*self.Ny):
            self.analyticalXDerivativeOfSurface[iCoord] = (self.A)*(self.M)*(self.M-1)*self.PDDOCoordinateMesh[iCoord,0]**(self.M-2)*\
                    (self.B)*self.PDDOCoordinateMesh[iCoord,1]**(self.N)
        self.analyticalXDerivativeOfSurface = self.analyticalXDerivativeOfSurface.reshape((self.Nx,self.Ny))

    def calculateAnalyticalYDerivativeOfSurface(self):
        self.analyticalYDerivativeOfSurface = np.zeros(self.Nx*self.Ny)
        for iCoord in range(self.Nx*self.Ny):
            self.analyticalYDerivativeOfSurface[iCoord] = (self.A)*self.PDDOCoordinateMesh[iCoord,0]**self.M*\
                    (self.B)*(self.N)*(self.N-1)*self.PDDOCoordinateMesh[iCoord,1]**(self.N-2)
        self.analyticalYDerivativeOfSurface = self.analyticalYDerivativeOfSurface.reshape((self.Nx,self.Ny))

    def calculateAnalyticalLaplacianOfSurface(self):
        self.analyticalLaplacianOfSurface = self.analyticalXDerivativeOfSurface + self.analyticalYDerivativeOfSurface

    def addNoise(self):
        noise = np.random.normal(0, 0.15, size= (self.Nx, self.Ny))
        self.surfaceNoisy = self.surface + noise

    def solve(self):
        self.createCoordinates()
        self.createSurface()
        self.calculateAnalyticalXDerivativeOfSurface()
        self.calculateAnalyticalYDerivativeOfSurface()
        self.calculateAnalyticalLaplacianOfSurface()
        self.addNoise()
