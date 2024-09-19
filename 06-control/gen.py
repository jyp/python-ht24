
def is_not_divisible_by_any(i,ps):
    for p in ps:
        if i % p == 0:
            return False
    return True

def primes():
    i = 2
    ps = []
    while True:
        if is_not_divisible_by_any(i,ps):
            ps.append(i)
            yield i
        i = i+1

for i in primes():
    print(i)
  


