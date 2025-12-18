import cv2
from .io_utils import ensure_uint8

# Fungsi untuk mengubah array gambar menjadi format file PNG dalam bentuk bytes
def encode_png(gray) -> bytes:
    gray = ensure_uint8(gray)
    ok, buf = cv2.imencode(".png", gray)
    if not ok:
        raise ValueError("Gagal encode PNG.")
    return buf.tobytes()