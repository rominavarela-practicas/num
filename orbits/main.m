clear all;
close all;
clc;

planet = 9;

% perihelium and aphelium in AU
switch(planet)
    case 1
        % Mercury
        au = [ 0.307, 0.446 ] ;
    case 2
        % Venus
        au = [ 0.718, 0.728 ] ;
    case 3
        % Earth
        au = [ 0.98, 1.1 ] ;
    case 4
        % Mars
        au = [ 1.38, 1.66 ] ;
    case 5
        % Jupiter
        au = [ 4.95, 5.46 ] ;
    case 6
        % Saturn
        au = [ 9.05, 10.12 ] ;
    case 7
        % Uranus
        au = [ 18.4, 20.1 ] ;
    case 8
        % Neptune
        au = [ 29.8, 30.4 ] ;
    case 9
        % Pluto
        au = [ 29.7, 49.3 ] ;
end

%% CALCULATE

[ a,b,c,e ] = ellipse_description( au(1) , au(2) );
[ x,y ] = ellipse_interpolation( a , b , 100 );

%% PLOT

figure;
hold on;

plot ( au(1) , 0 , 'mo');
plot ( a , 0 , 'kx');
plot( x , y , 'k');

switch(planet)
    case 1
        title('Mercury');
    case 2
        title('Venus');
    case 3
        title('Earth');
    case 4
        title('Mars');
    case 5
        title('Jupiter');
    case 6
        title('Saturn');
    case 7
        title('Uranus');
    case 8
        title('Neptune');
    case 9
        title('Pluto');
end

hold off;