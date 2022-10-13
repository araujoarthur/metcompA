from typing import List, Tuple
import numpy as np

dat = "0.21 13.60 0.46 15.76 0.82 19.32 1.58 29.96 1.96 35.09 2.64 42.68 3.18 50.64 3.35 53.62 3.86 56.93 4.26 61.51 5.05 70.19 5.58 76.54 5.92 82.28 6.34 86.00 7.05 97.42 7.28 96.58 8.24 112.37 8.42 110.60 8.80 115.76 9.46 125.09"
databular = dat.split(" ")
x = []
y = []
for i in range(0,len(databular)):
  if i%2 == 0:
    x.append(databular[i])
  else:
    y.append(databular[i])

def linFit(x:List[float], y:List[float]):
  x = np.array(x, float)
  y = np.array(y, float)
  x_ = np.mean(x)
  y_ = np.mean(y)
  xsqr_ = np.mean(x**2)
  xy_ = np.mean(x*y)

  alph = (xy_ - x_ * y_)/(xsqr_ - (x_**2))
  bet = (xsqr_ * y_ - x_ * xy_)/(xsqr_ - (x_**2))

  return (alph,bet)

print(linFit(x,y))

for i in y:
  print(i)
