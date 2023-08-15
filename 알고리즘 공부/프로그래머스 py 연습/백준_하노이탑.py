def f(n, first, mid, end):
  if(n == 1):
    print(first, end, sep = " ")
  else:
    f(n-1, first, end, mid)
    f(1, first, mid, end)
    f(n-1, mid, first, end)

n = int(input())
print(2**n-1)
if(n <= 20):
  f(n, 1, 2, 3)