
l1 = [1,2,3,4,5]
l2 = []
l3 = []

def move1(source,destination):
    disk = source.pop()
    destination.append(disk)
    print(l1)
    print(l2)
    print(l3)
    print("============")

def move_many(n, source, intermediate , destination):
    if n == 0:
        pass
    else:
       move_many(n-1, source, destination, intermediate)
       move1(source,destination)
       move_many(n-1, intermediate, source, destination)

move_many(5,l1,l2,l3)
