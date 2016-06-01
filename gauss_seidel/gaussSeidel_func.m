function [ r ] = gaussSeidel_func( C , R , E )
%GAUSSSEIDEL_FUNC Summary of this function goes here
%   C coeficient matrix, req: squared and diagonal dominant
%   R results matrix
%   E fault tolerance
debug = false;

r0 = R.*0;
r = R.*0;
len = size(C,1);

i=0;
e= 2;
    
    % while fault tolerance is not surpassed
    while(e>E)
        % for each row
        for row = 1:len
            % join result's matrix element
            r(row) = R(row);
            for col = 1:len
                if(col~=row)
                    % with each partial result not in diagonal
                    r(row) = r(row) - ( C(row,col) * r(col));
                end
            end
            % divide with diagonal element
            r(row) = r(row) / C(row,row);
        end
        
        % compute margin
        e= norm(r-r0)/norm(r);
        r0= r;
        
        if(debug)
            i= i+1;
            r.*1
        end
        
    end
    
    
    if(debug)
        disp(' ');
        disp(['   required margin: ' num2str(E)]);
        disp(['   final margin: ' num2str(e)]);
        disp(['   iterations: ' num2str(i)]);
    end
end

