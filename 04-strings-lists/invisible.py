
print("\t")
print(" ")

# character to number: ord
# number to character: chr
# character to bits

def int_to_binary(x):
  result = [] # empty list
  while x != 0:
     result.append(x % 2)
     x = x // 2
  result.reverse()
  return result


def justify_binary_8(x):
    n = 8 - len(x)
    return ([0] * n) + x

def binary_to_int(bits):
    b = bits[0]
    result = 0
    while len(bits) > 0:
        result = result*2 + bits[0]
        bits=bits[1:len(bits)]
    return result

def split_in_8_bits_groups(input):
    result = []
    while len(input) > 0:
        result.append(input[0:8])
        input = input[8:len(input)]
    result.reverse()
    return result

print (split_in_8_bits_groups([0] * 32))

# print(binary_to_int([0, 1, 0, 0, 0, 0, 0, 1]))

# print(justify_binary_8 (int_to_binary(65)))





