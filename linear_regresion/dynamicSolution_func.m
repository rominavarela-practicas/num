function [ func ] = dynamicSolution_func( x, y, sub )
%GENERALSOLUTION_FUNC Summary of this function goes here
%   Detailed explanation goes here
    
    %% Calculate X
    % apply each subFunction(x)
    nSub = numel(sub);
    
    X = [];
    for i = 1:nSub
        f = cell2mat(sub(i));
        X = [ X , arrayfun(f,x) ];
    end
    
    %% Calculate A
    A = inv(X' * X) * ( X' * y);
    
    %% Join Subfunctions
    % http://www.mathworks.com/matlabcentral/newsreader/view_thread/325818
    
    % subs =  { a1*sub1 , a2*sub2 , ... , aN*subN }
    subs = cell(nSub,1);
    for i = 1:nSub
        a = A(i);
        f = cell2mat(sub(i));
        subs{i} = @(x) a * f(x);
    end
    
    % func = (a1*sub1) + (a2*sub2) + (...) + (aN*subN)
    func = @(x) sum(cellfun(@(y) y(x), subs));
end

