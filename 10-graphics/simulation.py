import math
class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return str(self.x) + "," + str(self.y)
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    def __neg__(self):
        return self.scaled(-1)
    def scaled(self, scalar):
        return Vec(self.x * scalar, self.y * scalar)
    def __mul__(self, scalar): # this will be used when the scalar is the 2nd operand (v * s)
        return self.scaled(scalar)
    def __rmul__(self, scalar): # this will be used when the scalar is the 1st operand (s * v)
        return self.scaled(scalar)
    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)

class Particle:
    def __init__(self, pos, vel, mass):
        self.pos = pos
        self.vel = vel
        self.mass = mass
    def __repr__(self):
        return "Particle pos=" + str(self.pos) + " vel="+str(self.vel)
    def constant_gravity(self, dt):
        self.vel = self.vel + dt * Vec(0,-0.1)
    def accelerate(self, force, dt):
        self.vel = self.vel + (dt / self.mass) * force
    def inertial_move(self, dt):
        self.pos = self.pos + dt * self.vel

def set_circle_absolute_position(c, target_vector):
    print(c.getCenter())
    c.move(target_vector.x - c.getCenter().x,
           target_vector.y - c.getCenter().y)

class GraphicalParticle:
    def __init__(self, particle):
        self.p = particle
        point = Point(0,0)
        self.circle = Circle(point,3*math.sqrt(particle.mass))
        self.circle.setFill("magenta")
        self.circle.draw(win)
        self.graphical_update()
    def graphical_update(self):
        set_circle_absolute_position(self.circle,self.p.pos)
    
p0 = Particle(Vec(0,0), Vec(1,1), 10)
p1 = Particle(Vec(-10,0), Vec(-1,1), 1)
particles = [p0,p1]

from graphics import *
win = GraphWin("simulation" , 640, 480)
win.setCoords(-320, -240, 320, 240)

gparticles = []
for p in particles:
    gparticles.append(GraphicalParticle(p))

G = 2
timestep = 0.1
print(win.getKey())
while True:
    # Physical simulation
    # for p in particles:
    #     p.constant_gravity(timestep)
    for i in range(0,len(particles)):
        for j in range(i+1,len(particles)):
            p1 = particles[i]
            p2 = particles[j]
            d = p2.pos - p1.pos
            r = d.norm()
            unit = (1/r) * d
            f = G * p1.mass * p2.mass / (r**2)
            force = f * unit
            p1.accelerate(force, timestep)
            p2.accelerate(-force, timestep)
            
    
    for p in particles:
        p.inertial_move(timestep)
        
    # Graphical update
    for g in gparticles:
        g.graphical_update()
        

c.move(0,15)
print(win.getKey())
