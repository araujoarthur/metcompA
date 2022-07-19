x = int(input("Insert number: "))

def factorial(n):
  if n == 1:
    return n
  else:
    return n*factorial(n-1)
    
print(factorial(x))

