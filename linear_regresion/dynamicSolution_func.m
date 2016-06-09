function [ func ] = dynamicSolution_func( x, y, sub )
%GENERALSOLUTION_FUNC Summary of this function goes here
%   Detailed explanation goes here
    
    %% Calculate X
    % apply each subFunction(x)
    nSub = numel(sub);
    
    X = [];
    for i = 1:nSub
        f = inline(cell2mat(sub(i)));
        X = [ X , f(x) ];
    end
    
    %% Calculate A
    A = inv(X' * X) * ( X' * y);
    
    %% Join Subfunctions
    % (a1*sub1) + (a2-sub2) ... + (aN-subN)
    func = [ '(' , num2str(A(1)), '*', cell2mat(sub(1)) , ')' ];
    for i = 2:nSub
        func = [ func , ' + (' , num2str(A(1)), '* (', cell2mat(sub(i)) , '))'];
    end
    
    func = inline(func);
end

