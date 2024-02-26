close all;
clear all;

addpath('..\data')
addpath('C:\Users\docta\Documents\Thesis\FourthPDENoiseRemovalPDDO\data')
g20 = table2array(readtable('g20.csv'));
g02 = table2array(readtable('g02.csv'));


PDDOKernelMesh = table2array(readtable('PDDOKernelMesh.csv'));
%[X,Y] = meshgrid(PDDOKernelMesh(:,1),PDDOKernelMesh(:,2));
surface = table2array(readtable('surface.csv'));
%figure; plot(PDDOKernelMesh(:,1),PDDOKernelMesh(:,2),'o')

figure; surf(reshape(PDDOKernelMesh(:,1),[512 512]),reshape(PDDOKernelMesh(:,2),[512 512]),reshape(sqrt(surface),[512 512]))





dt = 0.00000001;
numSteps = 1*5000;
OGImage = imread('lena.png');
noisyImage = imread('noisyLena.png');
g20 = table2array(readtable('g20.csv'));
g02 = table2array(readtable('g02.csv'));
figure;
for i=0:numSteps
    filteredImage = conv2(double(noisyImage),g20+g02,'same');
    filteredImage = double(noisyImage) +  dt*filteredImage;
    noisyImage = filteredImage;
    imagesc(filteredImage);
    colormap gray;
end


%figure; imagesc(image);colormap gray