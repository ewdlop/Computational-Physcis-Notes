function [X] = ConformalMappingMath( U,~ )

[m,n]=size(U);
X=zeros(m,n);

for i=1:m
    X(m,1)=U(m,1);
    X(m,2)=U(m,2);
end
end

