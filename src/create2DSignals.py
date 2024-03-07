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

    def createCoordinates(self):
        indexing = 'xy'
        xCoords = np.arange(self.dx/2, self.l1, self.dx)
        yCoords = np.arange(self.dy/2, self.l2, self.dy)
        xCoords, yCoords = np.meshgrid(xCoords, yCoords, indexing=indexing)
        xCoords = xCoords.reshape(-1, 1)
        yCoords = yCoords.reshape(-1, 1)
        self.PDDOCoordinateMesh = np.array([xCoords[:,0], yCoords[:,0]]).T
    
    def createSphericalSurface(self):
        self.sphericalSurface = np.array((self.PDDOCoordinateMesh[:,0]-0.5)**2 + (self.PDDOCoordinateMesh[:,1]-0.5)**2).reshape((self.Nx,self.Ny))

    def createCylindricalSurface(self):
        self.cylindricalSurface = np.zeros(self.Nx*self.Ny)
        centerIndex = np.linalg.norm(np.array([self.PDDOCoordinateMesh[:,0]-0.5, \
                self.PDDOCoordinateMesh[:,1]-0.5]),axis=0).argmin()
        self.cylindricalSurface[np.where(np.linalg.norm(np.array([self.PDDOCoordinateMesh[:,0] - \
                self.PDDOCoordinateMesh[centerIndex,0], self.PDDOCoordinateMesh[:,1] - \
                self.PDDOCoordinateMesh[centerIndex,1]]),axis=0)<0.25)] = 1
        self.cylindricalSurface = self.cylindricalSurface.reshape((self.Nx,self.Ny))

    
    def createSurface(self):
        self.surface = np.zeros(self.Nx*self.Ny)
        for iCoord in range(self.Nx*self.Ny):
            self.surface[iCoord] = -3*self.PDDOCoordinateMesh[iCoord,0]**2+2*self.PDDOCoordinateMesh[iCoord,1]**2+1
        self.surface = self.surface.reshape((self.Nx,self.Ny))


    def addNoise(self):
        noise = np.random.normal(0, 0.15, size= (self.Nx, self.Ny))
        self.sphericalSurfaceNoisy = self.sphericalSurface + noise
        self.cylindricalSurfaceNoisy = self.cylindricalSurface + noise

    def solve(self):
        self.createCoordinates()
        self.createSphericalSurface()
        self.createCylindricalSurface()
        self.createSurface()
        self.addNoise()
