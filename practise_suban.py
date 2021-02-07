def table(n):

   for i in range (1,n+1):
       t = []
       for j in range(1,n+1):
            t.append(i*j)
       print(*t, sep ="   ")

table(10)