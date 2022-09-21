from typing import Callable

def simpleIntegral(f:Callable, inferior:float, superior:float, _N: int, ref="L"):
  dx = (superior - inferior)/_N
  res = 0
  if (ref == "L"):
    for i in range(0, _N):
      _x = inferior + i * dx # I = 0 -> x0, i = 1 -> x1 (x0 + dx), i = 2 -> x2 (x1 + dx ou x0 + 2dx) ...
      res = res + f(_x) * dx
    return res
  if (ref == "R"):
    for i in range(0, _N):
      _x = inferior + dx * (1 + i)
      res = res + f(_x) * dx
    return res

def trapezeIntegral(f:Callable, inferior:float, superior:float, _N:int):
  dx = (superior - inferior)/_N

  return (((f(inferior) + f(superior))/2) + sum([f(dx*i) for i in range(1,_N)])) * dx


def simpsonIntegral(f:Callable, inferior:float, superior:float, _N:int):
  h = (superior - inferior)/_N
  evenSum = 0
  oddSum = 0
  # Result Build Up
  for i in range(1,_N):
    if i%2 == 0:
      evenSum += f(inferior + i*h)
    else:
      oddSum += f(inferior + i*h)
    
  return h/3 * (f(superior) + f(inferior) + 4 * oddSum + 2 * evenSum)
  
      
      
