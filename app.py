import streamlit as st

# Setup dasar aplikasi
st.set_page_config(page_title="GUI Operasi & Filter", layout="wide")
st.title("GUI Operasi Citra")

# Input file gambar
up = st.file_uploader("Upload gambar (JPG/PNG)", type=["jpg", "jpeg", "png"])
if not up:
    st.info("Silakan upload gambar dulu.")
    st.stop()

st.success("Upload OK. Fitur menyusul.")

# Layout kolom untuk perbandingan gambar
c1, c2 = st.columns(2, gap="large")
with c1:
    st.subheader("Original")
with c2:
    st.subheader("Processed")

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

# Membuat 3 tab utama: untuk tampilan gambar, grafik histogram, dan simpan file
tab1, tab2, tab3 = st.tabs(["Preview", "Histogram", "Export"])

with tab1:
    # Mengatur layout 2 kolom di dalam tab Preview
    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.subheader("Original")   # Judul kolom kiri
    with c2:
        st.subheader("Processed")  # Judul kolom kanan