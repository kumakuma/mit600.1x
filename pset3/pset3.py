#
# -----MIT 6.00x - PSET 2 -----
#
# by Dan Smith - 27/6/2016
# dan.smith.me@gmail.com
#


def f(x):
	import math
	return 200*math.e**(math.log(0.5)/14.1 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
    result = 0
    if step < 1:
        numSteps = int((stop - start) * (1 / step))
    else:
        numSteps = int((stop - start) / step)

    currentStep = start
    for i in range(numSteps):
        area = step * f(currentStep)
        result += area
        currentStep += step
    return result

print(radiationExposure(0, 40, 1))
print(radiationExposure(72, 96, 0.4))
print(radiationExposure(14, 20, 0.1))