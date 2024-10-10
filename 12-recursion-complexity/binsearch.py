
def binsearch(x,ns):
    # return true if x is in ns, assuming ns is sorted.
    midindex = len(ns) // 2
    if len(ns) == 0:
        return False
    if ns[midindex] == x:
        return True
    elif  x < ns[midindex]:
        return binsearch(x,ns[0:midindex])
    else:
        return binsearch(x,ns[midindex+1:len(ns)])

print(binsearch(7,[1,3,5,6,7]))
