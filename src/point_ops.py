import numpy as np
import cv2
from .io_utils import ensure_uint8

def brightness_contrast(gray: np.ndarray, alpha: float, beta: int) -> np.ndarray:
    # Pastiin citra bertipe uint8
    gray = ensure_uint8(gray)

    # Atur contrast (alpha) dan brightness (beta)
    return cv2.convertScaleAbs(gray, alpha=float(alpha), beta=int(beta))

def gamma_correction(gray: np.ndarray, gamma: float) -> np.ndarray:
    gray = ensure_uint8(gray)  # menormalisasi citra
    return gray  # dikembalikan tanpa perubahan
def gamma_correction(gray: np.ndarray, gamma: float) -> np.ndarray:
    gray = ensure_uint8(gray)
    g = float(gamma)
    if g <= 0:
        g = 1.0
    inv = 1.0 / g
    table = np.array([(i/255.0) ** inv * 255 for i in range(256)], dtype=np.uint8)
    return cv2.LUT(gray, table)

def negative(gray: np.ndarray) -> np.ndarray:
    gray = ensure_uint8(gray)
    return 255 - gray

def threshold_binary(gray: np.ndarray, t: int) -> np.ndarray:
    gray = ensure_uint8(gray)
    return gray
