
from math import exp

# steal from manim

def sigmoid(x: float) -> float:
    r"""Returns the output of the logistic function.

    The logistic function, a common example of a sigmoid function, is defined
    as :math:`\frac{1}{1 + e^{-x}}`.

    References
    ----------
    - https://en.wikipedia.org/wiki/Sigmoid_function
    - https://en.wikipedia.org/wiki/Logistic_function
    """
    return 1.0 / (1 + exp(-x))

def smooth(t: float, inflection: float = 10.0) -> float:
    if t < 0:
        return 0
    elif t > 1:
        return 1
    error = sigmoid(-inflection / 2)
    return min(
        max((sigmoid(inflection * (t - 0.5)) - error) / (1 - 2 * error), 0),
        1,
    )
    
def ease_in_out_back(t: float) -> float:
    if t < 0:
        return 0
    elif t > 1:
        return 1
    c1 = 1.70158
    c2 = c1 * 1.525
    return (
        (pow(2 * t, 2) * ((c2 + 1) * 2 * t - c2)) / 2
        if t < 0.5
        else (pow(2 * t - 2, 2) * ((c2 + 1) * (t * 2 - 2) + c2) + 2) / 2
    )

def ease_out_back(t: float) -> float:
    if t < 0:
        return 0
    elif t > 1:
        return 1
    c1 = 0.30158
    c3 = c1 + 1
    return 1 + c3 * pow(t - 1, 3) + c1 * pow(t - 1, 2)