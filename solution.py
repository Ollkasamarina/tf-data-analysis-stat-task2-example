import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id =  399666500

def solution(p: float, x: np.array) -> tuple:
    alpha = (1 - p) / 2
    alpha1 = (1 + p) / 2
    l = x.size
    a, a1 = pow(alpha, 1 / l), pow(alpha1, 1 / l)
    x_max = x.max()
    return (x_max - 0.005) / a1 + 0.005, (x_max - 0.005) / a + 0.005
