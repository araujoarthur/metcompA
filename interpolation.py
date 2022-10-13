from typing import Callable, Union, List, Tuple
import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
import math
from itertools import combinations
import pandas as pd

#Originally Written in Notebook Format

dfG = {'Neville':[], 'Lagrange':[]}

def Lxi(xi:float,xj:float) -> Callable:
  return lambda x: (x - xj)/(xi - xj)

def possibleCombinations(N:float,P:int) -> int:
  """
    [Legacy. itertools' combinations does everthing]
    Function to get possible combinations of N numbers in P positions.
  """
  return int(math.factorial(N)/(math.factorial(P)*math.factorial(N-P))) # Combination


def getLagrangePoly(points:List[Tuple[float, float]], DEBUG=False) -> str:
  """
    Function to return a string of the interpolation polynomial.
    Written by araujoarthur @ 10/10/2022 - 23:13
  """
  iterations = len(points) # Amount of points being used to evaluate.
  iterationsRange = range(0, iterations) # Just for reusability.
  coeficients = {N:[] for N in iterationsRange} # Holding coeficients for x^0, x^1, ..., x^N-1, x^N

  def __SIGN__(degree:int):
    """
      Function to define the sign based on a) the degree of the polynomial and b) the degree of the evaluating element.
    """
    if (iterations%2 == 0):
       return -1 if(degree%2 == 0) else 1
    else: # i.e if iterations is NOT even
      return 1 if(degree%2 == 0) else -1
        
  ll = 0 # DEBUG
  for p in iterationsRange: # Iterate on every element on the list of points given  
    print("---------- L"+str(ll)+"------------") if DEBUG else None # DEBUG
    ll += 1 # DEBUG

    pair = points[p] # Select the p-th pair in the list.
    pointList = [sPair for sPair in points if sPair != pair] # Generates a list without the p-th point.
    under = 1 # Initialization to be used as product later.
    partialCoef = {N:[] for N in iterationsRange} # Auxiliar dict to calculate coeficients.
    xlist = list() # Going to be used as a list of xvalues for the current pair. [REF2]

    for selection in pointList: # Iterates over the evaluation list for the given pair (the one without the pair itself.)
      under *= (pair[0] - selection[0]) # Calculates the denominator of the fraction. 
      xlist.append(selection[0]) # [REF2] creation of the xlist.
    
    coeficientIterations = iterations-1 # Creating an iterating guide variable starting on the (p-2)-th element (if exists.)
    while coeficientIterations >= 0: # Iterate to build coeficients.
      elements = iterations - coeficientIterations - 1 # Iterates over N - 1 Elements, so we have a * x^0 + ... + f * x^N-2 + g * x^N-1 = P(x)
      lenXList = len(xlist) # Reusability.
      indexes = [i for i in range(0,lenXList)] # List of indexes (Preventing equal numbers to collapse the combination method [Though it's not necessary bc of uniqueness]).
      combs = [list(cc) for cc in combinations(indexes,elements)] if coeficientIterations != 0 else [indexes] # Creating a list of combination of indexes (except when dealing for x^0).
      
      print("Coeficient for:" + str(coeficientIterations) + " | Elements Multiplying: " + str(elements) + " | indexes: " + str(indexes) + "| Combinations:"+ str(combs) +" | Under: " + str(under)) if DEBUG else None # DEBUG
      
      summation = 0 # Set summation to 0 to calculate a new coef. 
      for comb in combs: # Iterate over combinations.
        print([xlist[idx] for idx in comb]) if DEBUG else None # DEBUG
        summation = summation + (__SIGN__(coeficientIterations) * np.prod([xlist[idx] for idx in comb])) # Sums the coeficients for the same x^J.
      coeficients[coeficientIterations].append(pair[1]*(summation)/under) # Add the coeficient to the coeficients's dictionary.
      coeficientIterations -= 1

      print("SUMMATION: " + str(summation)) if DEBUG else None # DEBUG
      print("COEFICIENT: " + str(pair[1]*summation/under)) if DEBUG else None #DEBUG
    print(coeficients) if DEBUG else None # DEBUG

  returnable = "" #
  for k,v in coeficients.items():
    if type(v) == list:
      v = sum(v)
    returnable = returnable + ("+" if v > 0 else "") +((str(v) + (("*x^"+ str(int(k))) if k != 0 else "") + " ") if v != 0 else "")

  return returnable
    
    
    

def lagrangePoly(points:List[Tuple[float, float]], x:float) -> float:
  """
    Function to intrpolate a point from N given points using lagrange's method
  """
  listL = list()

  for i in range(0,len(points)):
    pair = points[i]
    pointList = [sPair for sPair in points if sPair != pair]
    Li = list()
    for selection in pointList:
      Li.append(Lxi(pair[0], selection[0])(x)) # Confusing. Generates the series member and evaluates its value based on x, then appends to Li.
    listL.append(np.prod(Li))
    
  # Result Build Up:
  res = 0
  for i in range(0, len(listL)):
    res += listL[i]*points[i][1]
  
  return res

pointsToTest = [(-8.8,12.6), (-2.3,6.2), (2.7,8.4), (1.4,-14.9), (5.1,18.8)]
x2 = [pair[0] for pair in pointsToTest]
y2 = [pair[1] for pair in pointsToTest]
xaxis = np.linspace(-10,10,100)
yaxis = list()

pointsToTest2 = [(1,2),(2,3),(3,4),(4,5)]
x1 = [1,2,3,4]
y1 = [2,3,4,5]
print(getLagrangePoly(pointsToTest))
print(lagrange(x2,y2))


for i in xaxis:
  dfG['Lagrange'].append(lagrangePoly(pointsToTest,i))
  yaxis.append(lagrangePoly(pointsToTest,i))

plt.figure(0)
plt.plot(xaxis,yaxis, 'k', label= 'P(x)')  # plotando o polinômio interpolador
plt.scatter(xpoints,ypoints, label='dados') #plotando os pontos de entrada
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


pointsToTest3 = [
    (-8.8, 12.6),
    (-2.3, 6.2),
    (2.7, 8.4),
    (1.4, -14.9),
    (5.1, 18.8)
]

xpt = [pointsToTest[i][0] for i in range(0, len(pointsToTest3))]
ypt = [pointsToTest[i][1] for i in range(0, len(pointsToTest3))]

def Neville(points:List[Tuple[float,float]], xn:float):
  sizemtx = len(points)
  mtx = np.zeros((sizemtx, sizemtx))
  x = [points[i][0] for i in range(0, sizemtx)]
  for i in range(0, sizemtx):
    mtx[i][0] = points[i][1]
  
  for j in range(1, sizemtx):
    for i in range(0, sizemtx-j):
      #print("\n")
      #print("I: " + str(i) + " | J: " + str(j))
      mtx[i][j] = (1/(x[i]-x[i+j])) * ((xn - x[i+j])*mtx[i][j-1] - (xn - x[i])*mtx[i+1][j-1])  
  return mtx[0][sizemtx-1]

yax = list()

#Neville(pointsToTest,15)


for i in xaxis:
  dfG['Neville'].append(Neville(pointsToTest,i))
  yax.append(Neville(pointsToTest,i))

plt.figure(1)
plt.plot(xaxis,yax, 'k', label= 'Neville')  # plotando o polinômio interpolador
plt.plot(xaxis,yaxis, 'b', label= 'Lagrange')  # plotando o polinômio interpolador
plt.scatter(xpt,ypt, label='dados') #plotando os pontos de entrada
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

dfGpd = pd.DataFrame(dfG)
dfGpd['Diff'] = dfGpd['Neville'] - dfGpd['Lagrange']
display(dfGpd)
