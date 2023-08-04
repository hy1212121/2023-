a, b, c = map(int, input().split())

if (a==b==c):
  X = 10000+a*1000
elif (a==b!=c):
  X = 1000 + a * 100
elif b==c!=a:
  X = 1000 + b * 100
elif a==c!=b:
  X = 1000 + a * 100
elif a!=b!=c:
  if (a > b and a > c):
   X = a * 100
  elif (b > a and b > c):
   X = b * 100
  elif (c > b and c > a):
   X = c * 100
print(X)