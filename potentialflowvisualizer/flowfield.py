import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = "browser" # Feel free to disable this if you're running in notebook mode or prefer a different frontend.


class Flowfield:
    def __init__(self,
                 objects=[]
                 ):
        self.objects = objects

    def draw(self,
             scalar_to_plot="potential",  # "potential", "streamfunction", "xvel", "yvel", "velmag"
             x_points=np.linspace(-10, 10, 200),
             y_points=np.linspace(-10, 10, 200),
             show=True,
             ):
        X, Y = np.meshgrid(x_points, y_points)
        X_r = np.reshape(X, -1)
        Y_r = np.reshape(Y, -1)
        points = np.vstack((X_r, Y_r)).T

        scalar_to_plot_value = np.zeros_like(X_r)
        if scalar_to_plot == "velmag":
            x_vels = np.zeros_like(X_r)
            y_vels = np.zeros_like(X_r)
        for object in self.objects:
            if scalar_to_plot == "potential":
                scalar_to_plot_value += object.get_potential_at(points)
            elif scalar_to_plot == "streamfunction":
                scalar_to_plot_value += object.get_streamfunction_at(points)
            elif scalar_to_plot == "xvel":
                scalar_to_plot_value += object.get_x_velocity_at(points)
            elif scalar_to_plot == "yvel":
                scalar_to_plot_value += object.get_y_velocity_at(points)
            elif scalar_to_plot == "velmag":
                x_vels += object.get_x_velocity_at(points)
                y_vels += object.get_y_velocity_at(points)
            else:
                raise Exception
        if scalar_to_plot == "velmag":
            scalar_to_plot_value = np.sqrt(x_vels ** 2 + y_vels ** 2)

        # min = np.min(scalar_to_plot_value)
        # max = np.max(scalar_to_plot_value)
        min = np.nanpercentile(scalar_to_plot_value, 0)
        max = np.nanpercentile(scalar_to_plot_value, 100)

        fig = go.Figure()
        fig.add_trace(
            go.Contour(
                x=x_points,
                y=y_points,
                z=np.reshape(scalar_to_plot_value, X.shape),
                colorscale="Viridis",
                contours=dict(
                    start=min,
                    end=max,
                    size=(max - min) / 80
                ),
                colorbar=dict(
                    title=scalar_to_plot,
                    titleside="top",
                    ticks="outside"
                ),
            )
        )
        fig.update_layout(
            yaxis=dict(scaleanchor="x", scaleratio=1)
        )
        if show: fig.show()
