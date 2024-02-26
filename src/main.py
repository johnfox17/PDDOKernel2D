import numpy as np
import secondOrderDerivativePDDOKernel as PDDOKernel2ndOrder
import create2DSignals



def main():

    PDDOKernel2nd = PDDOKernel2ndOrder.secondOrderDerivativePDDOKernel()
    PDDOKernel2nd.solve()

    #np.savetxt('C:\\Users\\docta\\Documents\\Thesis\\PDDOKernel2D\\data\\g20.csv', PDDOKernel2nd.g20, delimiter=",")
    #np.savetxt('C:\\Users\\docta\\Documents\\Thesis\\PDDOKernel2D\\data\\g02.csv', PDDOKernel2nd.g02, delimiter=",")


    signals = create2DSignals.create2DSignals()
    signals.solve()

    np.savetxt('C:\\Users\\docta\\Documents\\Thesis\\PDDOKernel2D\\data\\PDDOKernelMesh.csv', signals.PDDOCoordinateMesh, delimiter=",")
    np.savetxt('C:\\Users\\docta\\Documents\\Thesis\\PDDOKernel2D\\data\\surface.csv', signals.sphericalSurface, delimiter=",")







if __name__ == "__main__":
    main()
