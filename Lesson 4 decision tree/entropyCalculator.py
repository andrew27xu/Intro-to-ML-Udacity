import math
pi=0.5
rest = 1-pi
entropy = -pi *math.log(pi,2) - rest * math.log(rest,2)
print "entropy:", entropy

inforGain = 1- entropy

print "information gain: ", inforGain