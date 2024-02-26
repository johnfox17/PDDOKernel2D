clear all;
close all;

addpath('../data');
mesh = table2array(readtable('mesh.csv'));
figure; plot(mesh(:,1),mesh(:,2),'o')
grid on;

xXis = reshape(table2array(readtable('xXis.csv')),[7 7]);
figure; plot(xXis,'o')
grid on;

yXis = reshape(table2array(readtable('yXis.csv')),[7 7]);
figure; plot(yXis,'o')
grid on;