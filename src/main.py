import numpy as np
import secondOrderDerivativePDDOKernel as PDDOKernel2ndOrder
import create2DSignals
from scipy import signal


def main():

    PDDOKernel2nd = PDDOKernel2ndOrder.secondOrderDerivativePDDOKernel()
    PDDOKernel2nd.solve()

    signals = create2DSignals.create2DSignals()
    signals.solve()

    
    np.savetxt('C:\\Users\\docta\\Documents\\Thesis\\PDDOKernel2D\\data\\PDDOKernelMesh.csv', PDDOKernel2nd.PDDOKernelMesh, delimiter=",")

    np.savetxt('C:\\Users\\docta\\Documents\\Thesis\\PDDOKernel2D\\data\\g20.csv', PDDOKernel2nd.g20, delimiter=",")
    np.savetxt('C:\\Users\\docta\\Documents\\Thesis\\PDDOKernel2D\\data\\g02.csv', PDDOKernel2nd.g02, delimiter=",")

    np.savetxt('C:\\Users\\docta\\Documents\\Thesis\\PDDOKernel2D\\data\\PDDOKernelCoordinateMesh.csv', signals.PDDOCoordinateMesh, delimiter=",")
    
    np.savetxt('C:\\Users\\docta\\Documents\\Thesis\\PDDOKernel2D\\data\\surface.csv', signals.surface, delimiter=",")
    
    np.savetxt('C:\\Users\\docta\\Documents\\Thesis\\PDDOKernel2D\\data\\analyticalXDerivativeOfSurface.csv', signals.analyticalXDerivativeOfSurface, delimiter=",")
    
    np.savetxt('C:\\Users\\docta\\Documents\\Thesis\\PDDOKernel2D\\data\\analyticalYDerivativeOfSurface.csv', signals.analyticalYDerivativeOfSurface, delimiter=",")
    
    np.savetxt('C:\\Users\\docta\\Documents\\Thesis\\PDDOKernel2D\\data\\analyticalLaplacianOfSurface.csv', signals.analyticalLaplacianOfSurface, delimiter=",")



if __name__ == "__main__":
    main()
