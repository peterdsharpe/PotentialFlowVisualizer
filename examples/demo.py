from potentialflowvisualizer import *

field = Flowfield(
    objects=[
        Freestream(u=1, v=0),
        Source(strength=5, x=-5, y=0),
        Vortex(strength=5, x=0, y=5),
        Doublet(strength=5, x=0, y=0, alpha=0),
        LineVortex(strength=-5, x1 = 0, y1 = -5, x2 = 5, y2 = 0),
        LineSource(strength=-5, x1 = 0, y1 = 5, x2 = 5, y2 = 0),
    ]
)

field.draw("potential")
field.draw("streamfunction")
field.draw("xvel")
field.draw("yvel")
field.draw("velmag")
