function [ magnitude ] = verctorMagnitude_func( V )
%VERCTORMAGNITUDE_FUNC Summary of this function goes here
%   V vector
    
    len = length(V);
    magnitude = 0;
    
    for i = 1:len
        magnitude= magnitude + (V(i)*V(i));
    end
    
    magnitude = sqrt(magnitude);

end

