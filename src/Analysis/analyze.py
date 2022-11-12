from mlxtend.plotting import heatmap
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd

from Equations.VerticalDisplacement import VerticalDisplacement
from Equations.Trigenometry import Trig
from Equations.QuadraticFormula import QuadraticFormula
from Equations.VerticalDisplacement import VerticalDisplacement
from Equations.DisplacementVelocityTime import DisplacementVelocityTime
from Equations.VertexTime import VertexTime

df = pd.read_csv('../Data/savant_metric_data.csv')

class Analyze:

    def solve(vi , la):

        """x = np.linspace(0, 1000)
        y = -0.00065386 * np.square(x - 441.66) + 127.55
        
        plt.plot(x, y)

        plt.autoscale()

        plt.show()"""

        vy = np.multiply(Trig.sin(la), vi)

        vx = np.multiply(Trig.cos(la), vi)

        at = QuadraticFormula.solve(-4.9, vy, 0)

        hd = DisplacementVelocityTime.solve(vx, at)

        vd = VerticalDisplacement.solve(vy)

        vertex_time = VertexTime.solve(vy)

        vhd = DisplacementVelocityTime.solve(vx, vertex_time)

        vertex = (vhd, vd)
        final_horizontal_displacement = (0, hd)

        print(vertex)
        print(final_horizontal_displacement)

Analyze.solve(46, 25)