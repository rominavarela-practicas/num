close all;
clear;
clc;

X = [0;1;2;3;4]
fX = [4;4;8;22;52]
granularity = 0.5;

gX = interpolation_func(X,fX,granularity)