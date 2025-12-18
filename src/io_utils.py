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
