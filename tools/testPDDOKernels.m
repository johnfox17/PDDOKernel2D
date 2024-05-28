close all;
clear all;

addpath('../data/output')
%addpath('C:\Users\docta\Documents\Thesis\FourthPDENoiseRemovalPDDO\data')
g10 = table2array(readtable('g10.csv'));
g01 = table2array(readtable('g01.csv'));
gGradient = table2array(readtable('gGradient.csv'));

g20 = table2array(readtable('g20.csv'));
g02 = table2array(readtable('g02.csv'));

SignalMesh = table2array(readtable('signalCoordinateMesh.csv'));
PDDOKernelCoordinateMesh1stOrder = table2array(readtable('PDDOKernelMesh1stOrder.csv'));
PDDOKernelCoordinateMesh2ndOrder = table2array(readtable('PDDOKernelMesh2ndOrder.csv'));
surface = table2array(readtable('surface.csv'));

analyticalFirstOrderXDerivativeOfSurface = table2array(readtable('analyticalFirstOrderXDerivativeOfSurface.csv'));
analyticalFirstOrderYDerivativeOfSurface = table2array(readtable('analyticalFirstOrderYDerivativeOfSurface.csv'));
analyticalGradientOfSurface = table2array(readtable('analyticalGradientOfSurface.csv'));

analyticalSecondOrderXDerivativeOfSurface = table2array(readtable('analyticalSecondOrderXDerivativeOfSurface.csv'));
analyticalSecondOrderYDerivativeOfSurface = table2array(readtable('analyticalSecondOrderYDerivativeOfSurface.csv'));
analyticalLaplacianOfSurface = table2array(readtable('analyticalLaplacianOfSurface.csv'));


GradientOfSurface = conv2(surface, gGradient,'same');
% analyticalLaplacianOfSurface =analyticalLaplacianOfSurface(4:end-3,4:end-3);
figure; plot(diag(GradientOfSurface(6:end-5,6:end-5)),'o')
hold on;
plot(diag(analyticalGradientOfSurface(6:end-5,6:end-5)),'^')
grid on;
title('PDDO Kernel Gradient of Surface (Diagonal)')
legend('PDDO','Analytical');




LaplacianOfSurface = conv2(surface, g20+g02,'same');
% analyticalLaplacianOfSurface =analyticalLaplacianOfSurface(4:end-3,4:end-3);
figure; plot(diag(LaplacianOfSurface(6:end-5,6:end-5)),'o')
hold on;
plot(diag(analyticalLaplacianOfSurface(6:end-5,6:end-5)),'^')
grid on;
title('PDDO Kernel Laplacian of Surface (Diagonal)')
legend('PDDO','Analytical');
ylim([0 5])

GradientOfSurface = GradientOfSurface(6:end-5,6:end-5);
GradientOfSurface = GradientOfSurface(:);
analyticalGradientOfSurface = analyticalGradientOfSurface(6:end-5,6:end-5);
analyticalGradientOfSurface = analyticalGradientOfSurface(:);

LaplacianOfSurface = LaplacianOfSurface(6:end-5,6:end-5);
LaplacianOfSurface = LaplacianOfSurface(:);
analyticalLaplacianOfSurface = analyticalLaplacianOfSurface(6:end-5,6:end-5);
analyticalLaplacianOfSurface = analyticalLaplacianOfSurface(:);


RMSEGradient = sqrt(mean((analyticalGradientOfSurface - GradientOfSurface).^2));
RMSELaplacian = sqrt(mean((analyticalLaplacianOfSurface - LaplacianOfSurface).^2));

