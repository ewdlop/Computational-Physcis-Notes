randomnumberUniformDistribution  = rand()*5+5
% Since rand function only generates numbers between 0 and 1, I have to scale it and
% move the center to 5.

randomnumberNormalDistribution  = randn
% The default mean for randn function is 0.
diceroll = randi([1 6])
% randi function genearates only integers and no decimals. [1 6] restraints the
% output to 1,2,3,4,5,or 6.