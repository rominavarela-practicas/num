function [ gY ] = interpolation_func( X , fX , granularity )
%INTERPOLATION_FUNC Summary of this function goes here
%   X
%   fX discrete values corresponding to each x
%   granularity
    debug = false;
    
    fNum = numel(fX);
    
    % fx holds the 1 last set
    % fX concats each computed set
    fx = fX;
    fX = [ fX , zeros(fNum,1) ];
    
    for j = 2:fNum
        
        for i = j:fNum
            fX(i,j) = (fx(i)-fx(i-1)) / (X(i)-X(i-j+1));
        end
        
        fx= fX(1:fNum,j);
        fX = [ fX , zeros(fNum,1) ];
    end
    
    % A = diagonal - 1
    A = diag(fX);
    A = A(1:fNum-1);
    
    % g(x) = a0 + a1(x-x0) + a2(x-x0)(x-x1) ...
    a = X(1);
    b = X(fNum);
    gX = linspace (a,b,fNum/granularity);
    gNum = numel(gX);
    
    gY = zeros(gNum,1);
    
    for gi = 1:gNum
         x = gX(gi);
        
        for ai = 1:numel(A)
            y = A(ai);
            for i = 1:ai-1
                y = y * (x - X(i));
            end
            gY(gi)= gY(gi) + y;
        end
    end
    
    if(debug)
        fX
        A
        figure;
        plot(gX,gY)
        xlabel('gX')
        ylabel('gY (ans)')
    end
end

