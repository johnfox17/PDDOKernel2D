import PDDOConstants
import numpy as np

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
        self.sphericalSurface = (self.PDDOCoordinateMesh[:,0]-0.5)**2 + (self.PDDOCoordinateMesh[:,1]-0.5)**2
    
    '''def createQuadraticFunction(self):
        self.quadraticFunction = -2*(self.coords - 0.5)**2 + 1
    
    def addNoise(self):
        noise = np.random.normal(0, 0.05, self.N)
        self.linearFunctionNoisy = self.linearFunction + noise
        self.linearFunctionNoisy = self.linearFunctionNoisy.reshape((self.N,1))
        self.quadraticFunctionNoisy = self.quadraticFunction + noise
        self.quadraticFunctionNoisy = self.quadraticFunctionNoisy.reshape((self.N,1))'''

    def solve(self):
        self.createCoordinates()
        self.createSphericalSurface()
        #self.createLinearFunction()
        #self.createQuadraticFunction()
        #self.addNoise()
