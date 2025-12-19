import cv2
import numpy as np

# Fungsi untuk mengubah ukuran citra (grayscale atau RGB) berdasarkan faktor skala
def resize_scale(img: np.ndarray, scale: float, interpolation: int = cv2.INTER_LINEAR) -> np.ndarray:
    if img is None:
        return img

    scale = float(scale)
    if scale <= 0:
        raise ValueError("scale harus > 0")

    if abs(scale - 1.0) < 1e-12:
        return img

    h, w = img.shape[:2]
    new_w = max(1, int(round(w * scale)))
    new_h = max(1, int(round(h * scale)))

    return cv2.resize(img, (new_w, new_h), interpolation=interpolation)