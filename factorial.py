v=int(input())
factorial=1
if (v==0):
    print(1)
else:
    for i in range(1,v+1):
      factorial=factorial*i
print(factorial)
