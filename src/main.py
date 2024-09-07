import numpy as np
import firstOrderDerivativePDDOKernel as PDDOKernel1stOrder
import secondOrderDerivativePDDOKernel as PDDOKernel2ndOrder
import firstOrderXFirstOrderYDerivativePDDOKernel as PDDOKernel11Order
import create2DSignals
from scipy import signal


def main():

    PDDOKernel1st = PDDOKernel1stOrder.firstOrderDerivativePDDOKernel()
    PDDOKernel1st.solve()
    
    PDDOKernel1st1st = PDDOKernel11Order.firstOrderXFirstOrderYDerivativePDDOKernel()
    PDDOKernel1st1st.solve()

    PDDOKernel2nd = PDDOKernel2ndOrder.secondOrderDerivativePDDOKernel()
    PDDOKernel2nd.solve()

    signals = create2DSignals.create2DSignals()
    signals.solve()
    
    #First Order Derivative
    np.savetxt('../data/output/PDDOKernelMesh1stOrder.csv', PDDOKernel1st.PDDOKernelMesh, delimiter=",")
    np.savetxt('../data/output/g10.csv', PDDOKernel1st.g10, delimiter=",")
    np.savetxt('../data/output/g01.csv', PDDOKernel1st.g01, delimiter=",")
    np.savetxt('../data/output/gGradient.csv', PDDOKernel1st.gGradient, delimiter=",")

    #First Order X and First Order X Derivatives
    np.savetxt('../data/output/g11.csv', PDDOKernel1st1st.g11, delimiter=",")
    
    #Second Order Derivative
    np.savetxt('../data/output/PDDOKernelMesh2ndOrder.csv', PDDOKernel2nd.PDDOKernelMesh, delimiter=",")
    np.savetxt('../data/output/g20.csv', PDDOKernel2nd.g20, delimiter=",")
    np.savetxt('../data/output/g02.csv', PDDOKernel2nd.g02, delimiter=",")
    np.savetxt('../data/output/gLaplacian.csv', PDDOKernel2nd.gLaplacian, delimiter=",")

    #Signal
    np.savetxt('../data/output/signalCoordinateMesh.csv', signals.PDDOCoordinateMesh, delimiter=",")
    np.savetxt('../data/output/surface.csv', signals.surface, delimiter=",")
    
    np.savetxt('../data/output/analyticalFirstOrderXDerivativeOfSurface.csv', signals.analyticalFirstOrderXDerivativeOfSurface, delimiter=",")
    np.savetxt('../data/output/analyticalFirstOrderYDerivativeOfSurface.csv', signals.analyticalFirstOrderYDerivativeOfSurface, delimiter=",")
    np.savetxt('../data/output/analyticalGradientOfSurface.csv', signals.analyticalGradientOfSurface, delimiter=",")

    np.savetxt('../data/output/analyticalSecondOrderXDerivativeOfSurface.csv', signals.analyticalSecondOrderXDerivativeOfSurface, delimiter=",")
    np.savetxt('../data/output/analyticalSecondOrderYDerivativeOfSurface.csv', signals.analyticalSecondOrderYDerivativeOfSurface, delimiter=",")
    np.savetxt('../data/output/analyticalLaplacianOfSurface.csv', signals.analyticalLaplacianOfSurface, delimiter=",")


if __name__ == "__main__":
    main()
