# Generators
def feed (l):
    yield l
l=['1..100','101..200','201..300','301..400']
load=feed(l)
print(next(load))
