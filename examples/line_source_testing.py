from potentialflowvisualizer import *

field = Flowfield(
    objects = [
        # Freestream(1,0)
    ]
)

field.objects.extend(
    [Source(0.10, x, 0) for x in np.linspace(0, 10, 10)]
)
#
# field.draw("potential")
# # field.draw("streamfunction")
# # field.draw("xvel")
# # field.draw("yvel")
#
# field2 = Flowfield(
#     objects = [
#         LineSource(1, 0, 0, 0.001, 0)
#     ]
# )
# field2.draw("potential")

# field = Flowfield(
#     objects = [
#         # Freestream(1,0)
#         Source(1,0,0)
#     ]
# )

field.draw("yvel")

field2 = Flowfield(
    objects = [
        LineSource(1, 0, 0, 10, 0)
    ]
)
field2.draw("yvel")