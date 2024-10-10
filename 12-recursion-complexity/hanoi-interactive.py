from graphics import *

DISC_SIZE    = 12
N = 20
tower_width = (N+1)*DISC_SIZE
tower_height = (N+0.5)*DISC_SIZE

win = GraphWin("Hanoi", tower_width*3, round(tower_height+DISC_SIZE), autoflush = False)
win.setCoords(0,0, tower_width*3, tower_height+DISC_SIZE)

def eventXY(event):
    # because graphics library is borked, we have to do reverse transformation of coordinates
    return (event.x, win.getHeight() - event.y)

# move a disc to an absolute position
def moveTo(self,x,y):
    w = self.p2.x - self.p1.x # because graphics library is borked ...
    self.move(x-self.p1.x-w//2, y-self.p1.y)

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
towers = [Tower(tower_width*(2*n+1)/2,0) for n in [0,1,2]]
def towerAt(x):
    t = int(x // tower_width)
    return towers[t]

# populate 1st tower 
for i in list(reversed(range(N))):
    width = (i+1)*DISC_SIZE
    d = Rectangle(Point(0,0),Point(width,DISC_SIZE))
    d.draw(win)
    d.setFill("pink")
    towers[0].append(d)

###################################
# interact with towers using mouse

# mouse release: drop the discs at tower under cursor
def drop(event,discs):
    tower = towerAt(event.x)
    while discs:
        tower.append(discs.pop())
    win.bind("<ButtonRelease>", None)
    win.bind("<Motion>", None)

# mouse move: show the moved stack at mouse position
def motion(event,discs):
    (x,y) = eventXY(event)
    for i,d in enumerate(reversed(discs)):
        moveTo(d,x,y + i*DISC_SIZE)

# mouse click: pick up discs
def onClick(event):
    (x,y) = eventXY(event)
    tower = towerAt(x)
    d = y // DISC_SIZE
    ds = []
    while len(tower.discs) > d:
        ds.append(tower.pop())
    win.bind("<Motion>", lambda e: motion(e,ds))
    win.bind("<ButtonRelease>", lambda e: drop(e,ds))
    
win.setMouseHandler(onClick)

while True:
    win.getMouse()
