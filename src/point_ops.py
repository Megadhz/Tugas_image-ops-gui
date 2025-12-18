import numpy as np
import cv2
from .io_utils import ensure_uint8

def brightness_contrast(gray: np.ndarray, alpha: float, beta: int) -> np.ndarray:
    # Pastiin citra bertipe uint8
    gray = ensure_uint8(gray)

    # Atur contrast (alpha) dan brightness (beta)
    return cv2.convertScaleAbs(gray, alpha=float(alpha), beta=int(beta))
