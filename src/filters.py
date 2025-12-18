import numpy as np
import cv2
from .io_utils import ensure_uint8

# Fungsi pembantu untuk memastikan ukuran kernel selalu ganjil
def _odd(k: int) -> int:
    k = int(k)
    if k < 1:
        k = 1
    return k if k % 2 == 1 else k + 1

# Fungsi untuk menghaluskan gambar menggunakan rata-rata tetangga (Box Blur)
def box_blur(gray, ksize):
    gray = ensure_uint8(gray)
    k = _odd(ksize)
    return cv2.blur(gray, (k, k))

# Fungsi untuk menghaluskan gambar menggunakan distribusi Gaussian
def gaussian_blur(gray, ksize, sigma):
    gray = ensure_uint8(gray)
    k = _odd(ksize)
    return cv2.GaussianBlur(gray, (k, k), float(sigma))

# Fungsi untuk mempertajam detail gambar (Sharpen)
def sharpen(gray):
    gray = ensure_uint8(gray)
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]], dtype=np.float32)
    return cv2.filter2D(gray, -1, kernel)

# Fungsi untuk mendeteksi tepi gambar menggunakan 8 tetangga (Edge Detection)
def edge_8(gray):
    gray = ensure_uint8(gray)
    kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]], dtype=np.float32)
    return cv2.filter2D(gray, -1, kernel)

# Fungsi untuk memberikan efek relief atau cetak timbul pada gambar (Emboss)
def emboss(gray):
    gray = ensure_uint8(gray)
    kernel = np.array([[-2,-1,0],[-1,1,1],[0,1,2]], dtype=np.float32)
    out = cv2.filter2D(gray, -1, kernel)
    return cv2.convertScaleAbs(out, alpha=1.0, beta=128)

# Fungsi untuk mendeteksi tepi gambar menggunakan 4 tetangga (Custom 4-neighbor)
def custom_4_neighbor(gray):
    gray = ensure_uint8(gray)
    kernel = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]], dtype=np.float32)
    return cv2.filter2D(gray, -1, kernel)