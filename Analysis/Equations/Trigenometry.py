import numpy as np

class Trig:

    """
    Calculates the sine and cosine given an angle
    """

    def sin(angle):

        r = np.radians(angle)

        s = np.sin(r)

        return s

    def cos(angle):

        r = np.radians(angle)

        c = np.cos(r)

        return c