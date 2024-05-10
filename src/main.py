import numpy as np
import secondOrderDerivativePDDOKernel as PDDOKernel2ndOrder
import create2DSignals
from scipy import signal


def main():

    PDDOKernel2nd = PDDOKernel2ndOrder.secondOrderDerivativePDDOKernel()
    PDDOKernel2nd.solve()

    signals = create2DSignals.create2DSignals()
    signals.solve()

    
    np.savetxt('../data/output/PDDOKernelMesh.csv', PDDOKernel2nd.PDDOKernelMesh, delimiter=",")

    np.savetxt('../data/output/g20.csv', PDDOKernel2nd.g20, delimiter=",")
    np.savetxt('../data/output/g02.csv', PDDOKernel2nd.g02, delimiter=",")

    np.savetxt('../data/output/PDDOKernelCoordinateMesh.csv', signals.PDDOCoordinateMesh, delimiter=",")
    
    np.savetxt('../data/output/surface.csv', signals.surface, delimiter=",")
    
    np.savetxt('../data/output/analyticalXDerivativeOfSurface.csv', signals.analyticalXDerivativeOfSurface, delimiter=",")
    
    np.savetxt('../data/output/analyticalYDerivativeOfSurface.csv', signals.analyticalYDerivativeOfSurface, delimiter=",")
    
    np.savetxt('../data/output/analyticalLaplacianOfSurface.csv', signals.analyticalLaplacianOfSurface, delimiter=",")

    np.savetxt('../data/output/xXis.csv', PDDOKernel2nd.xXis, delimiter=",")

    np.savetxt('../data/output/yXis.csv', PDDOKernel2nd.yXis, delimiter=",")



if __name__ == "__main__":
    main()
