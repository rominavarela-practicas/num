function [ func ] = leastSquares_func( x, y )
%LEASTSQUARES_FUNC Summary of this function goes here
%   Input
%   x independent values
%   y dependent values
%   Output
%   m - slope
%   b - constant
n = numel(x);
sumx = sum(x);
sumy = sum(y);
sumx2 = sum(x.^2);
sumy2 = sum(y.^2);
sumxy = sum(x.*y);

%m
m1 = (n*sumxy) - (sumx * sumy);
m2 = (n*sumx2) - (sumx^2);
m = m1/m2;

%b
b1 = (sumx * sumxy) - (sumy * sumx2);
b2 = (sumx^2) - (sumx2.*n);
b = b1 / b2;

% func
func = @(x) (m * x) + b ;

end

