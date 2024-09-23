def ptriples(n):
     result = []
     for a in range(1,n):
        for b in range(a,n):
               for c in range(b,n):
                   if a**2 + b**2 == c**2:
                         result.append((a,b,c))
     return result
print(ptriples(500))
