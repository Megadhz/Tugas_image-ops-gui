# NAMA TIM
- I Putu Megadhana Artabawa (230030031)
- I Putu Adi Dharma Prayoga (230030022)
- Komang Bagus Widiana (230030062)

---

# Image Ops GUI (Streamlit)

Aplikasi GUI sederhana berbasis **Streamlit** untuk praktik **operasi citra digital** (point operations & filtering).  
Aplikasi ini dibuat agar eksperimen pengolahan citra dapat dilakukan cepat lewat antarmuka web tanpa harus membuat GUI desktop manual.

## Fitur Utama
- Upload gambar (JPG/PNG)
- **Scaling (Resize)**: ubah skala gambar (0.1× sampai 3.0×) + pilihan interpolation
- **Mode Grayscale / RGB**
- **RGB Operations (Mode RGB)**:
  - RGB gain (R/G/B)
  - Preview channel (R / G / B)
  - Operasi & filter diterapkan **per-channel** (R, G, B)
- Point operations (grayscale):
  - alpha/beta (brightness & contrast)
  - gamma correction
  - negative
  - threshold binary
- Filters:
  - box blur
  - gaussian blur
  - sharpen
  - edge detect (8-neighbor)
  - emboss
  - custom 4-neighbor
- Histogram: perbandingan original vs processed (grayscale)
- Export hasil sebagai PNG

---

# Alasan Menggunakan Streamlit
1. **Cepat membuat GUI**: komponen UI (slider, checkbox, dropdown, tab) bisa dibuat dengan beberapa baris Python.
2. **Interaktif real-time**: perubahan parameter langsung memperbarui hasil pemrosesan, cocok untuk eksperimen operasi citra.
3. **Mudah dijalankan lintas perangkat**: cukup jalankan `streamlit run app.py`, tampil di browser (Windows/Mac/Linux).
4. **Fokus ke logika pengolahan citra**: tidak perlu setup rumit seperti framework GUI desktop, jadi fokus ke OpenCV/numpy.
5. **Struktur proyek rapi**: fungsi pemrosesan dipisah ke modul `src/`, sementara UI tetap ringkas di `app.py`.

---

# Struktur Folder
```text
Tugas_image-ops-gui/
  app.py
  requirements.txt
  README.md
  .gitignore
  src/
    __init__.py
    io_utils.py
    point_ops.py
    filters.py
    histogram.py
    export_utils.py
    resize_ops.py        
    rgb_ops.py           
  scripts/               (opsional)
```

---

# Cara Menjalankan

## 1) Clone repo
```bash
git clone https://github.com/Megadhz/Tugas_image-ops-gui.git
cd Tugas_image-ops-gui
```

## 2) Buat & aktifkan virtual environment
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Jika muncul error policy PowerShell, jalankan sekali:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 3) Install dependencies
```bash
pip install -r requirements.txt
```

## 4) Jalankan aplikasi
```bash
streamlit run app.py
```

Streamlit akan membuka browser otomatis. Jika tidak, cek URL di terminal (biasanya `http://localhost:8501`).

---

# Catatan Git (untuk kerja tim)
- Folder `.venv/` tidak boleh di-commit (sudah ada di `.gitignore`).
- Jika menambah library baru:
  1. `pip install <nama-library>`
  2. update `requirements.txt`
  3. commit `requirements.txt`

---

# Troubleshooting Singkat
- **ModuleNotFoundError**: pastikan venv aktif dan sudah `pip install -r requirements.txt`
- **Gagal baca gambar**: pastikan file benar-benar JPG/PNG (bukan file rusak)
- **Streamlit minta email**: boleh dikosongkan saja (tekan Enter)
