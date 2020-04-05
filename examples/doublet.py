from potentialflowvisualizer import *

field = Flowfield([
    Doublet(1, 0, 0, 0)
])

# field.draw("potential")
# field.draw("streamfunction")
field.draw("xvel")
field.draw("yvel")
# field.draw("velmag")
