function [nothing]= ConformalMapping( input_args )

  A = imread('Doge.jpeg');
  A = A(1:529,1:529,:);
  figure, 
  imshow(A);
  title('Original Image');
  
  conformal = maketform('custom', 2, 2, [], @ConformalMappingMath, []);
   
  uData = [  0.75/2   -0.75/2];  % Bounds for REAL(w)
  vData = [  0.75/2  -0.75/2];  % Bounds for IMAG(w)
  xData = [ -1.2    1.2 ];  % Bounds for REAL(z)
  yData = [  1.0   -1.0 ];  % Bounds for IMAG(z)
  
  B = imtransform( A, conformal, 'cubic', ...
                'UData', uData,'VData', vData,...
                'XData', xData,'YData', yData,...
                'SIZE', [529 529], 'FillValues', 255 );
  figure, 
  imshow(B);
  title('Transformed Image');
  
  
end

