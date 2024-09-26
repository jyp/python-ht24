
# matrices represented as lists of lists (rows) with NO SHARING of rows.



def zeros(n):
    return zeros_rectangular(n,n)

def zeros_rectangular(m,n):
    # return a matrix of dimensions n×m with zeros everywhere
    result = []
    for i in range(0,m):
        # reminder: [x] * n  == list of n references (pointers) to x.
        result.append([0] * n)
    return result

def identity(n):
    # return a matrix of dimensions n×n
    # with ones on diagonal and zeros everywhere else
    result = zeros(n)
    for i in range(0,n):
        result[i][i] = 1
    return result

def number_of_rows(A):
    return len(A)

def number_of_columns(A):
    return len(A[0])

def addition(A,B):
    assert number_of_rows(A) == number_of_rows(B)
    assert number_of_columns(A) == number_of_columns(B)
    m = number_of_rows(A)
    n = number_of_columns(A)
    result = zeros_rectangular(m,n)
    for i in range(0,m):
       for j in range(0,n):
           result[i][j] = A[i][j] + B[i][j]
    return result

A = [[1,2]]
B = [[3,4]]

print( addition(A,B) )
print (identity(6))
