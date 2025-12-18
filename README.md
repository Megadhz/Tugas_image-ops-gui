========================================
NAMA TIM
========================================
- I Putu Megadhana Artabawa (230030031)
- I Putu Adi Dharma Prayoga (230030022)
- Komang Bagus Widiana (230030062)




========================================
Image Ops GUI (Streamlit)
========================================

Aplikasi GUI sederhana untuk praktik operasi citra (point operations & filtering) berbasis notebook.
Fitur utama:
- Upload gambar (JPG/PNG)
- Point operations: alpha/beta, gamma, negative, threshold
- Filters: box blur, gaussian blur, sharpen, edge, emboss, custom 4-neighbor
- Histogram: perbandingan original vs processed
- Export hasil sebagai PNG

========================================
STRUKTUR FOLDER
========================================
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
  scripts/                 (opsional)

========================================
CARA MENJALANKAN 
========================================

1) Clone repo
  git clone https://github.com/Megadhz/Tugas_image-ops-gui.git
  cd Tugas_image-ops-gui

2) Buat & aktifkan virtual environment
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1

   Jika muncul error policy PowerShell, jalankan sekali:
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

3) Install dependencies
  pip install -r requirements.txt

4) Jalankan aplikasi
  streamlit run app.py

Streamlit akan membuka browser otomatis. Jika tidak, cek URL di terminal
(biasanya http://localhost:8501).

========================================
CATATAN GIT (untuk kerja tim)
========================================
- Folder .venv/ tidak boleh di-commit (sudah ada di .gitignore).
- Jika menambah library baru:
  1) pip install <nama-library>
  2) update requirements.txt
  3) commit requirements.txt

========================================
TROUBLESHOOTING SINGKAT
========================================
- ModuleNotFoundError: pastikan venv aktif dan sudah pip install -r requirements.txt
- Gagal baca gambar: pastikan file benar-benar JPG/PNG (bukan file rusak)
- Streamlit minta email: boleh dikosongkan saja (tekan Enter)
