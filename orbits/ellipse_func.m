function [ funcX, funcY ] = ellipse_func( a , b )

    funcX = @(theta) a + (2*a)*sin(theta);
    funcY = @(theta) (b)*cos(theta);

end

