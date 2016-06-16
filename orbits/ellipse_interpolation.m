function [ x , y ] = ellipse_interpolation( a , b , n )
    
    [ funcX, funcY ] = ellipse_func( a , b );
    
    theta = linspace( -pi , pi , n );
    x = arrayfun(funcX,theta);
    y = arrayfun(funcY,theta);
    
end

