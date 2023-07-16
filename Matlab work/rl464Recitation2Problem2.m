r1 = input('What is the value for the equatorial radius?');
r2 = input('What is the value for the polar radius?');
y=acos(r2/r1);
area=2*pi*(r1^2+r2^2*(log(cos(y)/(1-sin(y)))/(sin(y))));
apparea=4*pi*((r1+r2)/2)^2;
display('The actually area is:');
display(area)
display('The apporximation is:');
display(apparea)
r3=6378.137;
r4=6356.752;
y2=acos(r4/r3);
area2=2*pi*(r3^2+r3^2*(log(cos(y2)/(1-sin(y2)))/(sin(y2))));
apparea2=4*pi*((r3+r4)/2)^2;
display('For Earth,the actually area is(km^2)');
display(area2)
display('and the apporximation is:')
display(apparea2);
