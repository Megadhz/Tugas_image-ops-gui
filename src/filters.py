import numpy as np
import cv2
from .io_utils import ensure_uint8

def _odd(k: int) -> int:

    # Pastikan k bertipe integer
    k = int(k)

    # Jika k kurang dari 1, set ke 1
    if k < 1:
        k = 1

    # Jika k sudah ganjil, kembalikan
    # Jika genap, tambahkan 1 agar menjadi ganjil
    return k if k % 2 == 1 else k + 1

def box_blur(gray, ksize):

    # Pastikan gambar bertipe uint8
    gray = ensure_uint8(gray)

    # Pastikan ukuran kernel ganjil dan minimal 1
    k = _odd(ksize)

    # Blur dengan metode rata-rata
    return cv2.blur(gray, (k, k))

def gaussian_blur(gray, ksize, sigma):
    # Pastikan gambar bertipe uint8
    gray = ensure_uint8(gray)

    # Pastikan ukuran kernel ganjil dan minimal 1
    k = _odd(ksize)

    # Blur dengan distribusi Gaussian
    return cv2.GaussianBlur(gray, (k, k), float(sigma))
