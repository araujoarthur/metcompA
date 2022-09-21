from typing import Callable
import math
import numpy as np

def centeredDerivative(x: Callable, xi:float, dx: float) -> float:
  return (x(xi+dx) - x(xi - dx))/(2*dx)

def bisectionMethod(a:float, b:float, tolerance:float, function:Callable) -> list:

    if(abs(b-a) <= tolerance):
      return (a + b)/2
    else:
      xm = (a + b)/2
      intervals = [
          [a, xm],
          [xm, b]
      ]

      chosenInterval = list()

      if (function(a) * function(xm) < 0) and (function(b) * function(xm) > 0):
        chosenInterval = [a, xm]
      else:
        chosenInterval = [xm, b]
      # VAI DAR STACKOVERFLOW PARA INTERVALOS MUITO GRANDES!
      return bisectionMethod(chosenInterval[0], chosenInterval[1], tolerance, function)


def newtonMethod(a:float, tolerance:float, function:Callable):
  fa = function(a)
  fa_derivative = centeredDerivative(function, a, 2E-6)

  b = a - (fa/fa_derivative)
  if (abs(b-a) < tolerance):
    return b
  else:
    # VAI DAR STACKOVERFLOW SE HOUVEREM MUITAS TENTATIVAS!
    return newtonMethod(b, tolerance, function)

def secantMethod(a:float, b:float, tolerance:float, function:Callable):
  x = a - ((b-a)*function(a))/(function(b) - function(a))

  dif_xa = x - a
  dif_xb = x - b

  if((abs(dif_xa) <= tolerance) or (abs(dif_xb) <= tolerance)):
    return x
  elif(abs(dif_xa) < abs(dif_xb)):
    return secantMethod(a, x, tolerance, function)
  else:
    return secantMethod(x, b, tolerance, function)

  # MESMA COISA, MUITAS ITERAÇÕES = EXPLODE.


testParams =  [
    [lambda x: (math.cos(x) + np.log(x) + x), 1E-4], 
    [lambda x: (x*(math.e^(-x))) - (math.e^(-3)), 5E-6],
    [lambda x:-x**2+6*x+10, 1E-5]
    ]
    

print(bisectionMethod(0.1, 0.5, testParams[0][1], testParams[0][0]))
    



  
