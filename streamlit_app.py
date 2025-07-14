import streamlit as st
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Chemical Analysis App", layout="wide")

st.title("Chemical Analysis")
st.title("_chemical_ is :blue[cool] :sunglasses:")

# Buat tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Beranda", "Tabel Periodik", "Regresi", "Ketidakpastian", "Konversi", "Titrasi"])

# ==================== TAB 1 =====================
with tab1:
    st.header("📏 Regresi Linear dan Ketidakpastian dari Kalibrasi")

    st.subheader("📊 Data Kalibrasi")
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

        # Hitung regresi linier
        m = np.sum((x_vals - x_mean) * (y_vals - y_mean)) / np.sum((x_vals - x_mean) ** 2)
        b = y_mean - m * x_mean

        y_fit = m * x_vals + b
        Sy = sqrt(np.sum((y_vals - y_fit) ** 2) / (n_reg - 2))
        sum_sq_x = np.sum((x_vals - x_mean) ** 2)

        mu_reg = (Sy / m) * sqrt((1 / n_reg) + ((y_sampel - y_mean) ** 2 / (m ** 2 * sum_sq_x)))
        x_sampel = (y_sampel - b) / m

        st.success(f"Persamaan regresi: y = {m:.4f}x + {b:.4f}")
        st.info(f"Hasil konsentrasi sampel = {x_sampel:.2f} ± {mu_reg:.2f} (μ_reg)")

        # Gambar grafik linearitas
        fig, ax = plt.subplots()
        ax.scatter(x_vals, y_vals, label="Data Kalibrasi", color="blue")
        ax.plot(x_vals, y_fit, label=f"Regresi Linier", color="red")
        ax.axhline(y_sampel, color='green', linestyle='--', label=f"Abs Sampel = {y_sampel}")
        ax.set_xlabel("Konsentrasi (x)")
        ax.set_ylabel("Absorbansi (y)")
        ax.set_title("Kurva Kalibrasi")
        ax.legend()
        st.pyplot(fig)

    except Exception as e:
        mu_reg = 0
        x_sampel = None
        st.warning(f"Periksa input data. Kesalahan: {e}")

    if st.button("🎯 Hitung Ketidakpastian dari Regresi Saja"):
        try:
            uc = mu_reg
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
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/01/Periodic_table_large.png", use_column_width=True)

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
