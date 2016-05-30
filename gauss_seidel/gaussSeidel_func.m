function [ ans ] = gaussSeidel_func( C , R , E )
%GAUSSSEIDEL_FUNC Summary of this function goes here
%   C coeficient matrix, req: squared and diagonal dominant
%   R results matrix
%   E fault tolerance
    
    margin = 2;
    len = length(C);
    
    prev_ans = zeros(1,len);
    ans = zeros(1,len);
    
    % while fault tolerance is not surpassed
    while (margin > E )
        % for each row
        for row = 1:len
            % sum result's matrix element
            ans(row)= R(row);
            for col = 1:len
                if(col~=row)
                    % with each partial result not in diagonal
                    ans(row)= ans(row) - ( C(row,col) * ans(col));
                end
            end
            % divide with diagonal element
            ans(row)= ans(row) / C(row,row);

        end
        
        % compute margin
        margin = (verctorMagnitude_func( ans ) ...
                  - verctorMagnitude_func( prev_ans )) / ...
                  verctorMagnitude_func( ans );
        prev_ans = ans;
    end
    
    disp(['   final margin: ' num2str(margin)]);
    
end

