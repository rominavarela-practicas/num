function [ func ] = staticSolution_func( x, y, sub1, sub2 )
%GENERALSOLUTION_FUNC Summary of this function goes here
%   Detailed explanation goes here
    
    %% Calculate X
    % apply each subFunction(x)
    X = [sub1(x),sub2(x)];
    
    %% Calculate A
    A = inv(X' * X) * ( X' * y);
    
    %% Concat Subfunctions
    % (a1*sub1) + (a2-sub2) ... + (aN-subN)
    func = @(x) sub1(x) + sub2(x);
    
end