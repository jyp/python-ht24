s = "abcde"
print(len(s.ljust(1)))
print(s.rjust(23))


def decimal_to_binary(x):
  result = [] # empty list
  while x != 0:
     result.append(x % 2)
     # result = [x % 2] + result
     x = x // 2
  result.reverse()
  return result

def decimal_to_binary_string(x):
  result = "" # empty string
  while x != 0:
      if x % 2 == 0:
          result = "0" + result
      else:
          result = "1" + result
      x = x // 2
  return result 

 

# decimal_to_binary(30)
print(decimal_to_binary(234))
# print(decimal_to_binary_string(234))

 
