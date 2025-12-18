import streamlit as st
import matplotlib.pyplot as plt
from src.histogram import hist_gray
from src.io_utils import read_upload_to_bgr, to_gray
from src.point_ops import brightness_contrast, gamma_correction, negative, threshold_binary
from src.filters import box_blur, gaussian_blur, sharpen, edge_8, emboss, custom_4_neighbor
from src.export_utils import encode_png

# Setup dasar aplikasi
st.set_page_config(page_title="GUI Operasi & Filter", layout="wide")
st.title("GUI Operasi Citra")

# Input file gambar
up = st.file_uploader("Upload gambar (JPG/PNG)", type=["jpg", "jpeg", "png"])
if not up:
    st.info("Silakan upload gambar dulu.")
    st.stop()

st.success("Upload OK. Fitur menyusul.")

# Panel kontrol di sidebar
with st.sidebar:
    st.header("Point Operations")
    
    # Pengaturan dasar citra
    alpha = st.slider("Alpha (kontras)", 0.0, 3.0, 1.0, 0.05)
    beta  = st.slider("Beta (brightness)", -150, 150, 0, 1)
    gamma = st.slider("Gamma", 0.1, 5.0, 1.0, 0.05)

    # Opsi transformasi warna & biner
    use_negative = st.checkbox("Negative", False)
    use_thr = st.checkbox("Threshold", False)
    thr = st.slider("T", 0, 255, 128, 1, disabled=not use_thr)

with st.sidebar:
    st.header("Filters")
    
    # Menu dropdown untuk memilih jenis filter/kernel
    f = st.selectbox(
        "Pilih filter",
        ["None","Box Blur","Gaussian Blur","Sharpen","Edge","Emboss","Custom 4-neighbor"]
    )
    
    # Ukuran kernel (harus ganjil), aktif hanya untuk filter Blur
    ksize = st.slider("Kernel size (odd)", 1, 31, 3, 2, disabled=f not in ["Box Blur","Gaussian Blur"])
    
    # Parameter standar deviasi, aktif khusus untuk Gaussian Blur
    sigma = st.slider("Sigma", 0.0, 10.0, 0.0, 0.1, disabled=f != "Gaussian Blur")

# Logika pemrosesan citra
img_bgr = read_upload_to_bgr(up)
gray = to_gray(img_bgr)

out = brightness_contrast(gray, alpha, beta)
out = gamma_correction(out, gamma)
if use_negative:
    out = negative(out)
if use_thr:
    out = threshold_binary(out, thr)

if f == "Box Blur":
    out = box_blur(out, ksize)
elif f == "Gaussian Blur":
    out = gaussian_blur(out, ksize, sigma)
# (Bisa ditambahkan filter lain di sini nanti)

# Tampilan Output
# Membuat 3 tab utama: untuk tampilan gambar, grafik histogram, dan simpan file
tab1, tab2, tab3 = st.tabs(["Preview", "Histogram", "Export"])

with tab1:
    # Mengatur layout 2 kolom di dalam tab Preview
    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.subheader("Original")   # Judul kolom kiri
        st.image(gray, channels="GRAY", clamp=True)
    with c2:
        st.subheader("Processed")  # Judul kolom kanan
        st.image(out, channels="GRAY", clamp=True)

with tab2:
    # Hitung data histogram
    h1 = hist_gray(gray)
    h2 = hist_gray(out)
    
    # Setup plot matplotlib
    fig = plt.figure(figsize=(10, 4))
    plt.plot(h1, label="Original")
    plt.plot(h2, label="Processed")
    
    # Atur tampilan grafik
    plt.xlim(0, 255)
    plt.legend()
    
    # Render ke Streamlit
    st.pyplot(fig, clear_figure=True)

with tab3:
    # Siapkan antarmuka unduhan
    st.subheader("Unduh hasil")
    
    # Konversi array gambar ke format file bytes
    png_bytes = encode_png(out)
    
    # Tombol untuk mengunduh file ke lokal
    st.download_button(
        "Download hasil (PNG)",
        data=png_bytes,
        file_name="processed.png",
        mime="image/png"
    )

