
def newton_sqrt(r):
  epsilon = 0.000000000000001
  x = r
  previous = r + 1234
  # x != math.sqrt(r) # NO!
  # while previous != x: # convergence test # better, but NO!
  while abs(previous-x) > epsilon: # convergence test
      previous = x
      x = x/2 + (r/  (2*x))
  return x   

print(newton_sqrt(2))
