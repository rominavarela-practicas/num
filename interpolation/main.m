close all;
clear;
clc;

% X = [0;1;2;3;4]
% fX = [4;4;8;22;52]
X = [0,8,16,24,32,40]';
fX = [14.621,11.483,9.870,8.418,7.305,6.413]';
granularity = 0.5;

gX = interpolation_func(X,fX,1/8);
x = linspace(X(1),X(end),numel(gX));

%% PLOT

hold on;
xlabel('x');
ylabel('y');

plot(x,gX);
plot(X,fX,'ro');

hold off;