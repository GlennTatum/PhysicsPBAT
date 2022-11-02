import numpy as np
import matplotlib.pyplot as plt

class Plotter:

    def plot():

        plt.style.use('_mpl-gallery')

        # make data
        x = np.linspace(0, 10, 100)

        # Sample equations
        y = 4 + 2 * np.sin(2 * x)
        z = 4 + 2 * np.sin(4 * x)

        # Collection of Plots
        plots = [y, z]

        # plot
        fig, ax = plt.subplots()

        # Plot each equation in the collection of plots
        for p in plots:
            ax.plot(x, p, linewidth=2.0)

        ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
            ylim=(0, 8), yticks=np.arange(1, 8))

        plt.show()