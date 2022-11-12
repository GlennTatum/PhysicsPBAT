import numpy as np
import matplotlib.pyplot as plt

class QuadraticFormula:

    """
    This is the equation based of the Quadratic formula. It takes in 3 inputs
    from the quadratic equation ax^2 + bx + c = 0. https://en.wikipedia.org/wiki/Quadratic_formula
    """

    def solve(a, b, c):

        # Calculate the square root

        squared = np.sqrt(
            np.subtract(
                np.square(b), np.multiply(np.multiply(4, a), c)
            )
        )

        # Multiply 2a

        denominator = np.multiply(2, a)

        # Set b as a negative number

        b_negative = np.negative(b)

        # Divide to find the answer

        ans = np.divide(
            np.subtract(b_negative, squared), denominator
        )

        return ans