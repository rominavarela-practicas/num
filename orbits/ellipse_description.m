function [ a,b,c,e ] = ellipse_description( perihelium , aphelium )
    a = (perihelium + aphelium)/2;
    c = a - perihelium;
    b = sqrt( (a^2) - (c^2) );
    e = a/c;
end

