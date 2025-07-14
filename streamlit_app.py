import streamlit as st
from math import sqrt
import numpy as np

st.set_page_config(page_title="Chemical Analysis App", layout="wide")

st.title("Chemical Analysis")
st.title("_chemical_ is :blue[cool] :sunglasses:")

# Buat tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Beranda", "Tabel Periodik", "Regresi", "Ketidakpastian", "Konversi", "Titrasi"])

# ==================== TAB 1 =====================
with tab1:
    st.header("📏 Regresi Linear dan Ketidakpastian Pengukuran")

    col1, col2, col3 = st.columns(3)
    with col1:
        toleransi_timbangan = st.number_input("Toleransi Timbangan (g)", value=0.01, step=0.001)
    with col2:
        toleransi_pipet = st.number_input("Toleransi Pipet (mL)", value=0.05, step=0.001)
    with col3:
        toleransi_labu = st.number_input("Toleransi Labu Takar (mL)", value=0.12, step=0.01)

    st.subheader("📊 Data Hasil Uji Berulang")
    mode = st.radio("Pilih cara input:", ["Input SD langsung", "Input data hasil uji mentah"])

    if mode == "Input SD langsung":
        sd_repeatability = st.number_input("Standar Deviasi (SD) hasil uji", value=0.2, step=0.01)
        n_repeat = st.number_input("Jumlah Replikasi (n)", value=6, step=1)
    else:
        data_uji = st.text_area("Masukkan data hasil uji dipisah koma (misal: 5.1, 5.2, 5.0, 5.1)")
        try:
            hasil = list(map(float, data_uji.split(",")))
            n_repeat = len(hasil)
            sd_repeatability = np.std(hasil, ddof=1)
            st.success(f"SD hasil uji = {sd_repeatability:.4f}, n = {n_repeat}")
        except:
            st.warning("Masukkan data numerik yang valid, dipisahkan koma.")

    st.subheader("2️⃣ Ketidakpastian dari Regresi Kalibrasi")

    with st.expander("📈 Input Data Kurva Kalibrasi"):
        x_kal = st.text_input("Konsentrasi Standar (x), pisahkan koma", "2, 4, 6, 8, 10")
        y_kal = st.text_input("Absorbansi Standar (y), pisahkan koma", "0.145, 0.289, 0.429, 0.565, 0.712")
        y_sampel = st.number_input("Absorbansi Sampel", value=0.400, step=0.001)

        try:
            x_vals = np.array(list(map(float, x_kal.split(","))))
            y_vals = np.array(list(map(float, y_kal.split(","))))

            n_reg = len(x_vals)
            x_mean = np.mean(x_vals)
            y_mean = np.mean(y_vals)

            m = np.sum((x_vals - x_mean) * (y_vals - y_mean)) / np.sum((x_vals - x_mean) ** 2)
            b = y_mean - m * x_mean

            y_fit = m * x_vals + b
            Sy = sqrt(np.sum((y_vals - y_fit) ** 2) / (n_reg - 2))
            sum_sq_x = np.sum((x_vals - x_mean) ** 2)

            mu_reg = (Sy / m) * sqrt((1 / n_reg) + ((y_sampel - y_mean) ** 2 / (m ** 2 * sum_sq_x)))
            x_sampel = (y_sampel - b) / m

            st.success(f"Persamaan regresi: y = {m:.4f}x + {b:.4f}")
            st.info(f"Hasil konsentrasi sampel = {x_sampel:.2f} ± {mu_reg:.2f} (μ_reg)")
        except:
            mu_reg = 0
            x_sampel = None
            st.warning("Periksa input data regresi.")

    if st.button("🔍 Hitung Total Ketidakpastian"):
        try:
            u_timbangan = toleransi_timbangan / sqrt(3)
            u_pipet = toleransi_pipet / sqrt(3)
            u_labu = toleransi_labu / sqrt(3)
            u_repeat = sd_repeatability / sqrt(n_repeat)

            uc = sqrt(u_timbangan**2 + u_pipet**2 + u_labu**2 + u_repeat**2 + mu_reg**2)
            U = 2 * uc

            st.header("📤 Hasil Akhir")
            st.write(f"Ketidakpastian gabungan (**uc**) = **{uc:.4f}**")
            st.write(f"Ketidakpastian diperluas (**U**) = **{U:.4f}** (k = 2)")

            if x_sampel is not None:
                st.success(f"🔬 Hasil pengukuran akhir: **{x_sampel:.2f} ± {U:.2f}** (95% confidence level)")
        except:
            st.error("Perhitungan gagal. Periksa input datamu.")

# ==================== TAB 2 s.d. 6 =====================
with tab2:
    st.header("Tabel Periodik")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("Regresi Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab4:
    st.header("Ketidakpastian Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab5:
    st.header("Konversi Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab6:
    st.header("Titrasi Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
