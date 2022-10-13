from typing import Callable
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

# List Build Up

LIST_N = [2**i for i in range(2,26,2)]

integral_error = lambda exact,numeric: abs(exact - numeric)

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

  # Result Build Up
  firstTerm =  (f(superior) + f(inferior))/2
  summation =  sum([f(inferior + dx * i) for i in range(1,_N)])
  return (firstTerm + summation) * dx


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

# Block 2

def exercise2(): # Como são exercicios fazendo mais ou menos a mesma coisa, decidi garantir que não teria problema com escopo.
  def func(x):
    return 1/(x**2 + 1)
  limits = (-3,3)
  ERROR_DICT = {"N":LIST_N, "ERROR":[], "DX":[], "ALFA":[]}
  INDEX = 0
  for N in LIST_N:
    ERROR_DICT["ERROR"].append(math.log(integral_error(2.4980915447965088516598341545621802461556588082597934381093384735943039314745879099152179806408343191041337477590228283505585586, trapezeIntegral(func, limits[0], limits[1], N-1))))
    ERROR_DICT["DX"].append(math.log((limits[1] - limits[0])/N))
    ERROR_DICT["ALFA"].append(ERROR_DICT["ERROR"][INDEX]/ERROR_DICT["DX"][INDEX])
    print(INDEX)
    INDEX += 1

  print(ERROR_DICT)

  myDF = pd.DataFrame(ERROR_DICT)
  pd.set_option("display.precision", 16)
  display(myDF)

  plt.figure(0)
  fig, ax = plt.subplots()
  ax.plot(ERROR_DICT["DX"],ERROR_DICT["ERROR"], color="g", label="Centered Derivative")
  ax.grid()
  plt.xlabel("DX")
  plt.ylabel("ERROR")
  plt.title("Método do Trapézio")

  _err = []
  _dx = []
  _alph = []
  for k, v in ERROR_DICT.items():
    if k == "ERROR":
      print(k)
      _err = v
    if k == "DX":
      print(k)
      _dx = v
    if k == "ALFA":
      print(k)
      _alph = v
  
  for i in range(0,len(_err)):
    print(f'{_err[i]:.5E} & {_dx[i]:.5E} & {_alph[i]:.5E} \\\\')

exercise2()

# Block 3

def exercise3(): # Como são exercicios fazendo mais ou menos a mesma coisa, decidi garantir que não teria problema com escopo.
  def func(x):
    return 1/(x**2 + 1)
  limits = (-3,3)
  ERROR_DICT = {"N":LIST_N, "ERROR":[], "DX":[], "ALFA":[]}
  INDEX = 0
  for N in LIST_N:
    ERROR_DICT["ERROR"].append(math.log(integral_error(2.4980915447965088516598341545621802461556588082597934381093384735943039314745879099152179806408343191041337477590228283505585586, simpsonIntegral(func, limits[0], limits[1], N))))
    ERROR_DICT["DX"].append(math.log((limits[1] - limits[0])/N))
    ERROR_DICT["ALFA"].append(ERROR_DICT["ERROR"][INDEX]/ERROR_DICT["DX"][INDEX])
    print(INDEX)
    INDEX += 1

  print(ERROR_DICT)

  myDF = pd.DataFrame(ERROR_DICT)
  pd.set_option("display.precision", 16)
  display(myDF)

  plt.figure(0)
  fig, ax = plt.subplots()
  ax.plot(ERROR_DICT["DX"], ERROR_DICT["ERROR"], color="g")
  ax.grid()
  plt.xlabel("DX")
  plt.ylabel("ERROR")
  plt.title("Método do Simpson")

  _err = []
  _dx = []
  _alph = []
  for k, v in ERROR_DICT.items():
    if k == "ERROR":
      print(k)
      _err = v
    if k == "DX":
      print(k)
      _dx = v
    if k == "ALFA":
      print(k)
      _alph = v
  
  for i in range(0,len(_err)):
    print(f'{_err[i]:.5E} & {_dx[i]:.5E} & {_alph[i]:.5E} \\\\')
exercise3()

# Block 4

for N in LIST_N:
  print(str(N) + " \\\\")
