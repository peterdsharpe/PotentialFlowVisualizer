from potentialflowvisualizer import *

field = Flowfield(
    objects=[
        Freestream(1, 0),
        # Source(1, 0, 0),
        Vortex(-20, 0, 0),
        Doublet(-100, 0, 0, 0),
        # LineSource(1, 0, 0, 0, 5),
        # LineVortex(1, 0, 0, 0, 5),
    ]
)

# field.draw("potential")
field.draw("streamfunction")
# field.draw("xvel")
# field.draw("yvel")
# field.draw("velmag")
field.draw_streamlines()