import numpy as np
import cv2

def read_upload_to_bgr(uploaded_file) -> np.ndarray:

    # Membaca file upload dalam bentuk byte,
    # lalu mengubahnya menjadi array NumPy uint8
    data = np.frombuffer(uploaded_file.read(), dtype=np.uint8)

    # Decode byte array menjadi gambar berwarna (format BGR)
    img = cv2.imdecode(data, cv2.IMREAD_COLOR)

    # Jika gambar gagal dibaca (bukan file JPG/PNG valid)
    if img is None:
        raise ValueError("Gagal membaca gambar. Pastikan JPG/PNG valid.")

    # Mengembalikan gambar dalam bentuk NumPy array (BGR)
    return img

def to_gray(img_bgr: np.ndarray) -> np.ndarray:
    # Jika jumlah dimensi = 2, berarti gambar sudah grayscale
    if img_bgr.ndim == 2:
        return img_bgr

    # Jika gambar masih berwarna (BGR),
    # konversi menjadi grayscale
    return cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

def ensure_uint8(img: np.ndarray) -> np.ndarray:
    """
    Memastikan gambar bertipe uint8 (0–255).
    Jika belum, nilai akan dibatasi dan dikonversi.
    """

    # Jika tipe data sudah uint8, langsung kembalikan
    if img.dtype == np.uint8:
        return img

    # Batasi nilai piksel agar berada di rentang 0–255
    img = np.clip(img, 0, 255)

    # Konversi tipe data menjadi uint8
    return img.astype(np.uint8)

