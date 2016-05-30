%% exercice 1
clc;

C = [
        3.0, -0.1, -0.2; ...
        0.1, 7.0, -0.3; ...
        0.3, -0.2, 10.0
     ]
 
R = [
        7.85; ...
        -19.3; ...
        71.4
    ]

E = 0.001

x= gaussSeidel_func( C , R, E )

clear all;

%% exercice 2
clc;

C = [
        10, -1, 2, 0; ...
        -1, 11, -1, 3; ...
        2, -1, 10, -1; ...
        0, 3, -1, 8
     ]
 
R = [
        6; ...
        25; ...
        -11; ...
        15
    ]

E = 0.001

x= gaussSeidel_func( C , R, E )

clear all;