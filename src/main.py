import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

if __name__ == "__main__":
    # Create a grid
    n = 300
    x = np.linspace(-1, 1, n)
    y = np.linspace(-1, 1, n)
    X, Y = np.meshgrid(x, y)
    r = np.sqrt(X**2 + Y**2)
    # Define parameters for the wave equation
    m, n = 4, 3  # Mode numbers
    omega = 2 * np.pi  # Angular frequency
    # Define the standing wave pattern
    def chladni_pattern(t):
        Z = np.cos(m * np.pi * X) * np.cos(n * np.pi * Y) * np.cos(omega * t)
        return Z
    # Set up the figure
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_axis_off()
    im = ax.imshow(chladni_pattern(0), cmap="inferno", extent=[-1, 1, -1, 1])
    # Animation function
    def update(frame):
        Z = chladni_pattern(frame / 20)
        im.set_data(Z)
        return [im]
    ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)
    plt.show()
