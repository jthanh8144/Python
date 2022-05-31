import random as rd

def y(a,x):
  return a[0] + a[1]*x[1]+a[2]*x[2]+a[3]*x[3]

def e(a):
  sum = 0
  for x in data:
    sum += (x[0] - y(a,x))**2
  return sum

def e1(a,i):
  d = 0.000001
  a1 = a[:]
  a1[i] = a1[i]+d
  return (e(a1)-e(a))/d

def main():
  alpha = 1
  a = [rd.random() for i in range(4)]
  for _ in range(1000):
    a_new = a[:]
    for i in range(4):
      a_new[i] = a[i] - alpha * e1(a,i)
    if e(a_new)>e(a):
      alpha /= 2
    else:
      a = a_new
      alpha = alpha * 2
    
    print(alpha,a,e(a))
main()
