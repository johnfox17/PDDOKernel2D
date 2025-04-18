close all;
clear all;

addpath('../data/output')

g10 = table2array(readtable('g10.csv'));
g01 = table2array(readtable('g01.csv'));
gGradient = table2array(readtable('gGradient.csv'));

g20 = table2array(readtable('g20.csv'));
g02 = table2array(readtable('g02.csv'));

%Read coordinate meshes
PDDOKernelCoordinateMesh1stOrder = table2array(readtable('PDDOKernelMesh1stOrder.csv'));
PDDOKernelCoordinateMesh2ndOrder = table2array(readtable('PDDOKernelMesh2ndOrder.csv'));
SignalMesh = table2array(readtable('signalCoordinateMesh.csv'));

%Read Surfaces
surface = table2array(readtable('surface.csv'));
analyticalFirstOrderXDerivativeOfSurface = table2array(readtable('analyticalFirstOrderXDerivativeOfSurface.csv'));
analyticalFirstOrderYDerivativeOfSurface = table2array(readtable('analyticalFirstOrderYDerivativeOfSurface.csv'));
analyticalGradientOfSurface = table2array(readtable('analyticalGradientOfSurface.csv'));

analyticalSecondOrderXDerivativeOfSurface = table2array(readtable('analyticalSecondOrderXDerivativeOfSurface.csv'));
analyticalSecondOrderYDerivativeOfSurface = table2array(readtable('analyticalSecondOrderYDerivativeOfSurface.csv'));
analyticalLaplacianOfSurface = table2array(readtable('analyticalLaplacianOfSurface.csv'));

Nx = 512;
Ny = 512;

%Plot kernels
%g10
figure; surf( g10)
xlabel('x','FontSize',14)
ylabel('y','FontSize',14)
zlabel('z','FontSize',14)
% title('X Derivative PDDO Kernel (g^{10})')
ax = gca;
ax.FontSize = 14;
colormap winter;
%g01
figure; surf( g01)
xlabel('x','FontSize',14)
ylabel('y','FontSize',14)
zlabel('z','FontSize',14)
% title('Y Derivative PDDO Kernel (g^{01})')
ax = gca;
ax.FontSize = 14;
colormap winter;
%g20+g02
figure; surf(g20+g02)
xlabel('x','FontSize',14)
ylabel('y','FontSize',14)
zlabel('z','FontSize',14)

% title('Laplacian PDDO Kernel (g^{20} + g^{02})')
ax = gca;
ax.FontSize = 14;
colormap winter;
%Reshape Mesh
SignalMeshX = reshape(SignalMesh(:,1),[Nx Ny]);
SignalMeshY = reshape(SignalMesh(:,2),[Nx Ny]);
SignalXCoords = 1/(2*Nx):1/Nx:1;
SignalYCords = 1/(2*Ny):1/Ny:1;
%Plot original surface
%figure; imagesc(SignalMeshX, SignalMeshY, surface);
figure; imagesc(SignalXCoords, SignalYCords, surface);
xlabel('x_1','FontSize',14)
ylabel('y_2','FontSize',14)
colorbar;
ax = gca;
ax.FontSize = 14;
% title('Two-Dimensional Surface')

%Gradient in X
GradientXOfSurface = conv2(surface, g10,'same');
%Error Gradient of X
figure; imagesc(SignalXCoords, SignalYCords,abs(GradientXOfSurface(6:end-5,6:end-5)-analyticalFirstOrderXDerivativeOfSurface(6:end-5,6:end-5)))
colorbar;
% title('Derivative Respect to X Error');
grid on;
xlabel('x_1','FontSize',14)
ylabel('x_2','FontSize',14)

ax = gca;
ax.FontSize = 14;
%Gradient in Y
GradientYOfSurface = conv2(surface, g01,'same');
%Error Gradient of Y
figure; imagesc(SignalXCoords, SignalYCords,abs(GradientYOfSurface(6:end-5,6:end-5)-analyticalFirstOrderYDerivativeOfSurface(6:end-5,6:end-5)))
% title('Derivative Respect to Y Error');
grid on;
xlabel('x_1','FontSize',14)
ylabel('x_2','FontSize',14)
colorbar;
ax = gca;
ax.FontSize = 14;
%Laplacian
LaplacianOfSurface = conv2(surface, g20+g02,'same');
figure; imagesc(SignalXCoords, SignalYCords,abs(LaplacianOfSurface(6:end-5,6:end-5)-analyticalLaplacianOfSurface(6:end-5,6:end-5)));
% title('Laplacian Error');
grid on;
xlabel('x_1','FontSize',14)
ylabel('x_2','FontSize',14)
colorbar;
ax = gca;
ax.FontSize = 14;

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


% figure; plot(diag(GradientXOfSurface(6:end-5,6:end-5)),'o')
% hold on;
% plot(diag(analyticalFirstOrderXDerivativeOfSurface(6:end-5,6:end-5)),'^')
% grid on;
% title('PDDO Kernel Derivative Respect to X of Surface (Diagonal)')
% legend('PDDO','Analytical');

% figure; plot(diag(GradientYOfSurface(6:end-5,6:end-5)),'o')
% hold on;
% plot(diag(analyticalFirstOrderYDerivativeOfSurface(6:end-5,6:end-5)),'^')
% grid on;
% title('PDDO Kernel Derivative Respect to Y of Surface (Diagonal)')
% legend('PDDO','Analytical');

% figure; plot(diag(LaplacianOfSurface(6:end-5,6:end-5)),'o')
% hold on;
% plot(diag(analyticalLaplacianOfSurface(6:end-5,6:end-5)),'^')
% grid on;
% title('PDDO Kernel Laplacian of Surface (Diagonal)')
% legend('PDDO','Analytical');
% ylim([0 5])




