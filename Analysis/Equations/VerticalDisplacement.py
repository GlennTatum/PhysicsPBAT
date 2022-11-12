import numpy as np

class VerticalDisplacement:

    """
    Calculates the Vertical displacment (y-coordinate) of the vertex. Uses the
    equation Vf^2 = Vi^2 + 2ad. This equation assumes vf = 0 as we are solving
    for the vertical displacement of the vertex.
    """

    def solve(vi):

        g = 19.6 # 2(9.8) / 2ad

        visqr = np.square(vi)

        ans = np.divide(visqr, g)

        return ans