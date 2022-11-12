import numpy as np

class VertexTime:

    """
    Calculates the time of when the vertex is reached with the equation
    t = -b/2a
    """

    def solve(b):

        b_negative = np.negative(b)

        ans = np.divide(b_negative, -9.8)

        return ans