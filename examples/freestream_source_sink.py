from potentialflowvisualizer import *

field = Flowfield([
    Freestream(1, 0),
    Source(10, -3, 0),
    Source(-10, 3, 0),
])

field.draw("potential")
field.draw("streamfunction")
field.draw("xvel")
field.draw("yvel")
field.draw("velmag")
