import numpy as np
from .io_utils import ensure_uint8

def hist_gray(gray):
    gray = ensure_uint8(gray)
    return np.bincount(gray.flatten(), minlength=256)