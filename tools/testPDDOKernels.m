close all;
clear all;

addpath('..\data')
addpath('C:\Users\docta\Documents\Thesis\FourthPDENoiseRemovalPDDO\data')
g20 = table2array(readtable('g20.csv'));
g02 = table2array(readtable('g02.csv'));
PDDOKernelMesh = table2array(readtable('PDDOKernelMesh.csv'));
PDDOKernelCoordinateMesh = table2array(readtable('PDDOKernelCoordinateMesh.csv'));
surface = table2array(readtable('surface.csv'));
analyticalXDerivativeOfSurface = table2array(readtable('analyticalXDerivativeOfSurface.csv'));
analyticalYDerivativeOfSurface = table2array(readtable('analyticalYDerivativeOfSurface.csv'));
analyticalLaplacianOfSurface = table2array(readtable('analyticalLaplacianOfSurface.csv'));


LaplacianOfSurface = conv2(surface, g20+g02,'same');
% LaplacianOfSurface = LaplacianOfSurface(4:end-3,4:end-3);
% analyticalLaplacianOfSurface =analyticalLaplacianOfSurface(4:end-3,4:end-3);
figure; plot(diag(LaplacianOfSurface),'o')
hold on;
plot(diag(analyticalLaplacianOfSurface),'^')
grid on;
title('Laplacian of Surface')
legend('PDDO','Analytical');

xDerivativeOfSurface = conv2(surface, g20,'same');
xDerivativeOfSurface = xDerivativeOfSurface(4:end-3,4:end-3);
analyticalXDerivativeOfSurface = analyticalXDerivativeOfSurface(4:end-3,4:end-3);
figure; plot(diag(xDerivativeOfSurface),'o')
hold on;
plot(diag(analyticalXDerivativeOfSurface),'^')
grid on;
title('Second Derivative Respect to X of Surface')
legend('PDDO','Analytical');

yDerivativeOfSurface = conv2(surface, g20,'same');
yDerivativeOfSurface = yDerivativeOfSurface(4:end-3,4:end-3);
analyticalYDerivativeOfSurface =analyticalYDerivativeOfSurface(4:end-3,4:end-3);
figure; plot(diag(yDerivativeOfSurface),'o')
hold on;
plot(diag(analyticalYDerivativeOfSurface),'^')
grid on;
title('Second Derivative Respect to Y of Surface')
legend('PDDO','Analytical');


