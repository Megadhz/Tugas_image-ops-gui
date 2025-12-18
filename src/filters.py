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
