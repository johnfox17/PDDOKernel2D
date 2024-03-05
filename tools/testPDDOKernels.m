close all;
clear all;

addpath('..\data')
addpath('C:\Users\docta\Documents\Thesis\FourthPDENoiseRemovalPDDO\data')
% g20 = table2array(readtable('g20.csv'));
% g02 = table2array(readtable('g02.csv'));


PDDOKernelMesh = table2array(readtable('PDDOKernelMesh.csv'));
sphericalSurface = table2array(readtable('sphericalSurface.csv'));
sphericalSurfaceNoisy = table2array(readtable('sphericalSurfaceNoisy.csv'));

cylindricalSurface = table2array(readtable('cylindricalSurface.csv'));
cylindricalSurfaceNoisy = table2array(readtable('cylindricalSurfaceNoisy.csv'));

figure; surf(sphericalSurface)
figure; imagesc(sphericalSurfaceNoisy); colormap gray;
figure; surf(sphericalSurfaceNoisy)

figure; surf(cylindricalSurface)
figure; imagesc(cylindricalSurface); colormap gray;
figure; imagesc(cylindricalSurfaceNoisy); colormap gray;
figure; surf(cylindricalSurfaceNoisy)


dt = 0.000000001;
numSteps = 4*5000;
g20 = table2array(readtable('g20.csv'));
g02 = table2array(readtable('g02.csv'));


% 
% for i=0:numSteps
%     filteredImage = conv2(sphericalSurfaceNoisy,g20+g02,'same');
%     filteredImage = sphericalSurfaceNoisy +  dt*filteredImage;
%     sphericalSurfaceNoisy = filteredImage;
% 
% end
% figure; imagesc(filteredImage); colormap gray;
% figure; surf(filteredImage);



for i=0:numSteps
    filteredImage = conv2(cylindricalSurfaceNoisy,g20+g02,'same');
    filteredImage = cylindricalSurfaceNoisy +  dt*filteredImage;
    cylindricalSurfaceNoisy = filteredImage;
    
end
figure; imagesc(filteredImage); colormap gray;
figure; surf(filteredImage);



%figure; imagesc(image);colormap gray