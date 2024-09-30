


class C:
    def f(self,x):
        pass
def g(c,x):
    pass
c = C()
c.f(1)
# f(c,1) # wrong
C.f(c,1)
# c.g(1) # wrong
g(c,1)
# C.g(c,1) # wrong

print("ok")

