import numpy as np
import secondOrderDerivativePDDOKernel as PDDOKernel2ndOrder
import create2DSignals
from scipy import signal


def main():

    PDDOKernel2nd = PDDOKernel2ndOrder.secondOrderDerivativePDDOKernel()
    PDDOKernel2nd.solve()

    signals = create2DSignals.create2DSignals()
    signals.solve()


    np.savetxt('C:\\Users\\docta\\Documents\\Thesis\\PDDOKernel2D\\data\\g20.csv', PDDOKernel2nd.g20, delimiter=",")
    np.savetxt('C:\\Users\\docta\\Documents\\Thesis\\PDDOKernel2D\\data\\g02.csv', PDDOKernel2nd.g02, delimiter=",")

    np.savetxt('C:\\Users\\docta\\Documents\\Thesis\\PDDOKernel2D\\data\\PDDOKernelMesh.csv', signals.PDDOCoordinateMesh, delimiter=",")
    np.savetxt('C:\\Users\\docta\\Documents\\Thesis\\PDDOKernel2D\\data\\sphericalSurface.csv', signals.sphericalSurface, delimiter=",")
    
    np.savetxt('C:\\Users\\docta\\Documents\\Thesis\\PDDOKernel2D\\data\\cylindricalSurface.csv', signals.cylindricalSurface, delimiter=",")

    np.savetxt('C:\\Users\\docta\\Documents\\Thesis\\PDDOKernel2D\\data\\sphericalSurfaceNoisy.csv', signals.sphericalSurfaceNoisy, delimiter=",")

    np.savetxt('C:\\Users\\docta\\Documents\\Thesis\\PDDOKernel2D\\data\\cylindricalSurfaceNoisy.csv', signals.cylindricalSurfaceNoisy, delimiter=",")
    np.savetxt('C:\\Users\\docta\\Documents\\Thesis\\PDDOKernel2D\\data\\surface.csv', signals.surface, delimiter=",")



if __name__ == "__main__":
    main()
