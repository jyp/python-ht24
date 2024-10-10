
from graphics import *

DISC_SIZE    = 12
N = 20
tower_width = (N+1)*DISC_SIZE
tower_height = (N+0.5)*DISC_SIZE

win = GraphWin("Hanoi", tower_width*3, round(tower_height+DISC_SIZE), autoflush = False)
win.setCoords(0,0, tower_width*3, tower_height+DISC_SIZE)

# move a disc to an absolute position
def moveTo(self,x,y):
    w = self.p2.x - self.p1.x # because graphics library is borked ...
    self.move(x-self.p1.x-w//2, y-self.p1.y)
    update(50)

# see hanoi-graphics.py
class Tower:
    def __init__(self, x, y):
        self.discs = []
        self.x = x
        self.y = y
        stake = Rectangle(Point(x-DISC_SIZE/4,y), Point(x+DISC_SIZE/4,y+tower_height) )
        stake.setFill("black")
        stake.draw(win)
    def append(self, disc):
        moveTo(disc, self.x,self.y + DISC_SIZE*len(self.discs))
        self.discs.append(disc)
    def pop(self):
        disc = self.discs.pop()
        return disc

# place towers
towers = [Tower(tower_width*(2*n+1)/2,0)
          for n in [0,1,2]]

# populate 1st tower 
for i in list(reversed(range(N))):
    width = (i+1)*DISC_SIZE
    d = Rectangle(Point(0,0),Point(width,DISC_SIZE))
    d.draw(win)
    d.setFill("pink")
    towers[0].append(d)


def move1(source,destination):
    disk = source.pop()
    destination.append(disk)
    print("move")

def move_many(n, source, intermediate , destination):
    if n == 0:
        pass
    else:
       move_many(n-1, source, destination, intermediate)
       move1(source,destination)
       move_many(n-1, intermediate, source, destination)

move_many(N,towers[0],towers[1],towers[2])
