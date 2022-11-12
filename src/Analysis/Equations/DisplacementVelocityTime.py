import numpy as np

class DisplacementVelocityTime:

    """
    The equation d = vi(t)
    """

    def solve(vi, t):

        ans = np.multiply(vi, t)

        return ans
