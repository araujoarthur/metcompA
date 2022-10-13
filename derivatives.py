 from typing import Callable
 import pandas as pd
 import numpy as np
 import math
 import matplotlib.pyplot as plt
  
 def right_derivative(x: Callable, xi:float, dx: float) -> float:
  return (x(xi+dx) - x(xi))/dx
  
def derivativeError(num: float, an: float) -> float:
  return abs(an - num)/abs(an)

def centered_derivative(x: Callable, xi:float, dx: float) -> float:
  return (x(xi+dx) - x(xi - dx))/(2*dx)


# Data Analysis & Plot. Originally Written in Notebook Format

#variations = np.logspace(0, -16, num=160)
variations = np.logspace(0, -64, num=1600, base=2.0)
print(variations)
dataDict = dict()
dataDict['x'] = list()
dataDict['DX'] = list()
dataDict['RightDerivative'] = list()
dataDict['CenteredDerivative'] = list()
dataDict['ErrCen'] = list()
dataDict['ErrRig'] = list()

def analyticDeriv(x:float):
  return 27*(math.sin(x) + math.cos(x))
analytic = analyticDeriv(3)


for variation in variations:
  cd = centered_derivative(lambda x: x**3 * math.sin(x), 3, variation)
  rd = right_derivative(lambda x: x**3 * math.sin(x), 3, variation)
  dataDict['CenteredDerivative'].append(cd)
  dataDict['RightDerivative'].append(rd)
  dataDict['x'].append(3)
  dataDict['DX'].append(variation)
  dataDict['ErrCen'].append(derivativeError(cd, analytic))
  dataDict['ErrRig'].append(derivativeError(rd, analytic))

pd.set_option("display.precision", 16)

dframe = pd.DataFrame(dataDict)
display(dframe)



plt.figure(0)
fig, ax = plt.subplots()
ax.semilogx(variations, dataDict['CenteredDerivative'], color="g", label="Centered Derivative")
ax.semilogx(variations, dataDict['RightDerivative'], color="r", label="Right Derivative")
ax.semilogx(variations, [analytic for i in range(0, 1600)], color="b", label = "Analytic")
ax.grid()
ax.set_xscale('log')
plt.legend()
plt.title("Centered vs Right Derivatives [BASE 2]")
plt.xlabel("∆X")
plt.ylabel("f'(3)")
plt.show()

plt.figure(1)
fig2, ax2 = plt.subplots()
ax2.semilogx(variations, dataDict['ErrCen'], color="g", label="Error in Centered Derivative")
ax2.semilogx(variations, dataDict['ErrRig'], color="r", label="Error in Right Derivative")
ax2.grid()
ax2.set_xscale('log')
ax2.set_yscale('log')
plt.legend()
plt.title("Centered vs Right Derivatives Errors [BASE 2]")
plt.xlabel("∆X")
plt.ylabel("Error")
plt.show()
