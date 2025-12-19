import streamlit as st
import matplotlib.pyplot as plt
from src.histogram import hist_gray
from src.io_utils import read_upload_to_bgr, to_gray
from src.point_ops import brightness_contrast, gamma_correction, negative, threshold_binary
from src.filters import box_blur, gaussian_blur, sharpen, edge_8, emboss, custom_4_neighbor
from src.export_utils import encode_png
from src.resize_ops import resize_scale
from src.rgb_ops import bgr_to_rgb, rgb_to_bgr, adjust_rgb_gain, extract_channel, apply_per_channel

# Setup dasar aplikasi
st.set_page_config(page_title="GUI Operasi & Filter", layout="wide")
st.title("GUI Operasi Citra")

# Input file gambar
up = st.file_uploader("Upload gambar (JPG/PNG)", type=["jpg", "jpeg", "png"])
if not up:
    st.info("Silakan upload gambar dulu.")
    st.stop()

st.success("Upload OK. Fitur menyusul.")

# Panel Scaling + RGB
with st.sidebar:
    st.header("Scaling & RGB")

    mode = st.radio("Mode", ["Grayscale", "RGB"], index=0)

    scale = st.slider("Scale", 0.10, 3.00, 1.00, 0.05)

    interp_name = st.selectbox(
        "Interpolation",
        ["Nearest", "Linear", "Cubic", "Area"],
        index=1
    )
    interp_map = {
        "Nearest": 0,  # cv2.INTER_NEAREST
        "Linear": 1,   # cv2.INTER_LINEAR
        "Cubic": 2,    # cv2.INTER_CUBIC
        "Area": 3,     # cv2.INTER_AREA
    }

    # NOTE: OpenCV constants: NEAREST=0, LINEAR=1, CUBIC=2, AREA=3
    interpolation = interp_map[interp_name]

    r_gain = st.slider("R gain", 0.00, 3.00, 1.00, 0.05, disabled=(mode != "RGB"))
    g_gain = st.slider("G gain", 0.00, 3.00, 1.00, 0.05, disabled=(mode != "RGB"))
    b_gain = st.slider("B gain", 0.00, 3.00, 1.00, 0.05, disabled=(mode != "RGB"))

    ch_preview = st.selectbox(
        "Preview channel",
        ["None", "R", "G", "B"],
        index=0,
        disabled=(mode != "RGB")
    )

# Panel kontrol di sidebar
with st.sidebar:
    st.header("Point Operations")

    alpha = st.slider("Alpha (kontras)", 0.0, 3.0, 1.0, 0.05)
    beta  = st.slider("Beta (brightness)", -150, 150, 0, 1)
    gamma = st.slider("Gamma", 0.1, 5.0, 1.0, 0.05)

    use_negative = st.checkbox("Negative", False)
    use_thr = st.checkbox("Threshold", False)
    thr = st.slider("T", 0, 255, 128, 1, disabled=not use_thr)

with st.sidebar:
    st.header("Filters")

    f = st.selectbox(
        "Pilih filter",
        ["None","Box Blur","Gaussian Blur","Sharpen","Edge","Emboss","Custom 4-neighbor"]
    )

    ksize = st.slider("Kernel size (odd)", 1, 31, 3, 2, disabled=f not in ["Box Blur","Gaussian Blur"])
    sigma = st.slider("Sigma", 0.0, 10.0, 0.0, 0.1, disabled=f != "Gaussian Blur")


# Logika pemrosesan: resize di BGR -> mode RGB / grayscale
img_bgr = read_upload_to_bgr(up)

# Resize/scale 
img_bgr = resize_scale(img_bgr, scale, interpolation=interpolation)

# Fungsi pipeline grayscale kamu (biar dipakai ulang)
def _pipeline_gray(gray_img):
    out = brightness_contrast(gray_img, alpha, beta)
    out = gamma_correction(out, gamma)
    if use_negative:
        out = negative(out)
    if use_thr:
        out = threshold_binary(out, thr)

    if f == "Box Blur":
        out = box_blur(out, ksize)
    elif f == "Gaussian Blur":
        out = gaussian_blur(out, ksize, sigma)
    elif f == "Sharpen":
        out = sharpen(out)
    elif f == "Edge":
        out = edge_8(out)
    elif f == "Emboss":
        out = emboss(out)
    elif f == "Custom 4-neighbor":
        out = custom_4_neighbor(out)

    return out

# Branch mode
if mode == "RGB":
    rgb = bgr_to_rgb(img_bgr)

    # RGB ops utama (gain)
    rgb2 = adjust_rgb_gain(rgb, r_gain, g_gain, b_gain)

    # Terapkan ops + filter yang ada ke RGB secara per-channel
    out_rgb = apply_per_channel(rgb2, _pipeline_gray)

    # Untuk histogram: bikin grayscale dari RGB original (setelah resize) & output
    gray = to_gray(rgb_to_bgr(rgb))              # original gray (scaled)
    out_gray_for_hist = to_gray(rgb_to_bgr(out_rgb))

else:
    gray = to_gray(img_bgr)
    out = _pipeline_gray(gray)


# Tampilan Output
tab1, tab2, tab3 = st.tabs(["Preview", "Histogram", "Export"])

with tab1:
    c1, c2 = st.columns(2, gap="large")

    with c1:
        st.subheader("Original")
        if mode == "RGB":
            st.image(rgb, clamp=True)
        else:
            st.image(gray, channels="GRAY", clamp=True)

    with c2:
        st.subheader("Processed")
        if mode == "RGB":
            if ch_preview != "None":
                ch_img = extract_channel(out_rgb, ch_preview)
                st.image(ch_img, channels="GRAY", clamp=True, caption=f"Channel {ch_preview}")
            else:
                st.image(out_rgb, clamp=True)
        else:
            st.image(out, channels="GRAY", clamp=True)

with tab2:
    # Histogram
    if mode == "RGB":
        h1 = hist_gray(gray)
        h2 = hist_gray(out_gray_for_hist)

        fig = plt.figure(figsize=(10, 4))
        plt.plot(h1, label="Original (gray from RGB)")
        plt.plot(h2, label="Processed (gray from RGB)")
        plt.xlim(0, 255)
        plt.legend()
        st.pyplot(fig, clear_figure=True)
    else:
        h1 = hist_gray(gray)
        h2 = hist_gray(out)

        fig = plt.figure(figsize=(10, 4))
        plt.plot(h1, label="Original")
        plt.plot(h2, label="Processed")
        plt.xlim(0, 255)
        plt.legend()
        st.pyplot(fig, clear_figure=True)

with tab3:
    st.subheader("Unduh hasil")

    if mode == "RGB":
        # encode_png
        png_bytes = encode_png(rgb_to_bgr(out_rgb))
        fname = "processed_rgb.png"
    else:
        png_bytes = encode_png(out)
        fname = "processed.png"

    st.download_button(
        "Download hasil (PNG)",
        data=png_bytes,
        file_name=fname,
        mime="image/png"
    )
