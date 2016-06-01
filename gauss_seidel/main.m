%% exercice 1
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

x= gaussSeidel_func( C , R, 0.1 )

clear all;

%% exercice 2
clc;

C = [
        4.0, -1.0, -1.0; ...
        -2.0, 6.0, 1.0; ...
        -1.0, 1.0, 7.0
     ]
 
R = [
        3.0; ...
        9.0; ...
        -6.0
    ]

x= gaussSeidel_func( C , R, 0 )

clear all;