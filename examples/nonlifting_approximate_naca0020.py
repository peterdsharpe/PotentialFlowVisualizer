from potentialflowvisualizer import *


def cosspace(min=0, max=1, n_points=50):
    mean = (max + min) / 2
    amp = (max - min) / 2

    return mean + amp * np.cos(np.linspace(np.pi, 0, n_points))


# Body Geometry definition
x = cosspace(-5, 5, 51)
c = np.max(x) - np.min(x)
x0 = np.min(x)
y = 0.2 * c * 10 * (
        + 0.2969 * ((x - x0) / c) ** 0.5
        - 0.1260 * ((x - x0) / c)
        - 0.3516 * ((x - x0) / c) ** 2
        + 0.2843 * ((x - x0) / c) ** 3
        - 0.1036 * ((x - x0) / c) ** 4
)
dx = np.diff(x)
dy = np.diff(y)

# Flow properties
V = 100
alpha = 10
alpha_rad = np.radians(alpha)

field = Flowfield([
    Freestream(V * np.cos(alpha_rad), V * np.sin(alpha_rad))
])

field.objects.extend(
    [LineSource(V * dy[i], x[i], 0, x[i + 1], 0) for i in range(len(x) - 1)]
)
field.objects.extend(
    [Doublet(2 * V * y[i] * alpha_rad * dx[i], (x[i] + x[i+1])/2, 0, np.radians(90)) for i in range(len(x) - 1)]
)

field.draw("streamfunction")
