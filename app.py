import streamlit as st

st.set_page_config(page_title="GUI Operasi & Filter", layout="wide")
st.title("GUI Operasi Citra")

up = st.file_uploader("Upload gambar (JPG/PNG)", type=["jpg", "jpeg", "png"])
if not up:
    st.info("Silakan upload gambar dulu.")
    st.stop()

st.success("Upload OK. Fitur menyusul.")

c1, c2 = st.columns(2, gap="large")
with c1:
    st.subheader("Original")
with c2:
    st.subheader("Processed")