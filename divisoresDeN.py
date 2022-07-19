n = int(input('Insert N: '))
x = int(input('Insert floor: '))
y = int(input('Insert ceil: '))

if x > y:
  print("Floor can not be bigger than ceil")
elif x == y:
  print('Floor and ceil can not be equal')
elif not(y > n):
  print('N can not be bigger than ceil')
else:
  for i in range(x,y):
    if n%i == 0:
      #Não exatamente uma saida, mas o mesmo processo pode popular uma array 
      print(i)
