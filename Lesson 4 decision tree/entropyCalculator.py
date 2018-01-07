import math
pi=0.333
rest = 1-pi
entropy = -pi *math.log(pi,2) - rest * math.log(rest,2)
print entropy