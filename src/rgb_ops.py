import numpy as np
import cv2

# Fungsi untuk mengubah urutan warna dari BGR (OpenCV) ke RGB
def bgr_to_rgb(img_bgr: np.ndarray) -> np.ndarray:
    if img_bgr is None:
        return img_bgr
    if img_bgr.ndim != 3 or img_bgr.shape[2] != 3:
        return img_bgr
    return cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# Fungsi untuk mengubah urutan warna dari RGB ke BGR (OpenCV)
def rgb_to_bgr(img_rgb: np.ndarray) -> np.ndarray:
    if img_rgb is None:
        return img_rgb
    if img_rgb.ndim != 3 or img_rgb.shape[2] != 3:
        return img_rgb
    return cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

# Fungsi untuk mengatur penguatan (gain) intensitas pada masing-masing saluran R, G, dan B
def adjust_rgb_gain(img_rgb: np.ndarray, r_gain: float, g_gain: float, b_gain: float) -> np.ndarray:
    if img_rgb is None:
        return img_rgb
    if img_rgb.ndim != 3 or img_rgb.shape[2] != 3:
        return img_rgb

    x = img_rgb.astype(np.float32)
    x[..., 0] *= float(r_gain)  # R
    x[..., 1] *= float(g_gain)  # G
    x[..., 2] *= float(b_gain)  # B
    x = np.clip(x, 0, 255)
    return x.astype(np.uint8)

# Fungsi untuk mengekstrak salah satu saluran warna (R, G, atau B) menjadi citra grayscale
def extract_channel(img_rgb: np.ndarray, ch: str) -> np.ndarray:
    if img_rgb is None:
        return img_rgb
    if img_rgb.ndim != 3 or img_rgb.shape[2] != 3:
        return img_rgb

    ch = ch.upper()
    idx = {"R": 0, "G": 1, "B": 2}.get(ch, 0)
    return img_rgb[..., idx].astype(np.uint8)

# Fungsi untuk menerapkan fungsi pemrosesan grayscale ke setiap saluran RGB secara terpisah lalu menggabungkannya kembali
def apply_per_channel(img_rgb: np.ndarray, fn_gray) -> np.ndarray:
    if img_rgb is None:
        return img_rgb
    if img_rgb.ndim != 3 or img_rgb.shape[2] != 3:
        return img_rgb

    r = fn_gray(img_rgb[..., 0])
    g = fn_gray(img_rgb[..., 1])
    b = fn_gray(img_rgb[..., 2])

    out = np.stack([r, g, b], axis=2)
    return out.astype(np.uint8)