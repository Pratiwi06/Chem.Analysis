import streamlit as st
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Chemical Analysis App", layout="wide")

st.title("Chemical Analysis")
st.title("_chemical_ is :blue[cool] :sunglasses:")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Beranda", "Tabel Periodik", "Regresi", "Ketidakpastian", "Konversi", "Titrasi"])

# ==================== TAB 1 =====================
with tab1:
    st.header("Selamat datang di Aplikasi Analisis Kimia")
    st.write("Gunakan tab di atas untuk berbagai fitur analisis kimia.")

# ==================== TAB 2 =====================
with tab2:
    st.header("Tabel Periodik")
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/01/Periodic_table_large.png", use_column_width=True)

# ==================== TAB 3 - REGRESI =====================
with tab3:
    st.header("📊 Regresi Linear dan Ketidakpastian Regresi")

    with st.expander("📈 Input Data Kalibrasi"):
        x_input = st.text_input("Konsentrasi Standar (x), pisahkan koma", "2, 4, 6, 8, 10")
        y_input = st.text_input("Absorbansi Standar (y), pisahkan koma", "0.145, 0.289, 0.429, 0.565, 0.712")
        y_sampel = st.number_input("Absorbansi Sampel", value=0.400, step=0.001)

    # Validasi dan proses
    try:
        x_vals = np.array([float(i.strip()) for i in x_input.split(",") if i.strip() != ""])
        y_vals = np.array([float(i.strip()) for i in y_input.split(",") if i.strip() != ""])

        if len(x_vals) != len(y_vals):
            st.error("❌ Jumlah data x dan y tidak sama.")
        elif len(x_vals) < 2:
            st.error("❌ Minimal 2 pasang data diperlukan untuk regresi.")
        else:
            n = len(x_vals)
            x_mean = np.mean(x_vals)
            y_mean = np.mean(y_vals)

            # Hitung regresi linier
            m = np.sum((x_vals - x_mean) * (y_vals - y_mean)) / np.sum((x_vals - x_mean)**2)
            b = y_mean - m * x_mean
            y_fit = m * x_vals + b

            # Standar deviasi residual dan ketidakpastian dari regresi
            Sy = np.sqrt(np.sum((y_vals - y_fit) ** 2) / (n - 2))
            sum_sq_x = np.sum((x_vals - x_mean)**2)
            mu_reg = (Sy / m) * np.sqrt((1 / n) + ((y_sampel - y_mean) ** 2 / (m ** 2 * sum_sq_x)))
            x_sampel = (y_sampel - b) / m

            # Korelasi
            r = np.corrcoef(x_vals, y_vals)[0, 1]
            R2 = r ** 2

            # Output hasil regresi
            st.success(f"Persamaan regresi: y = {m:.4f}x + {b:.4f}")
            st.info(f"Hasil konsentrasi sampel = {x_sampel:.2f} ± {mu_reg:.2f} (μ_reg)")
            st.write(f"Koefisien Korelasi (r): **{r:.4f}**")
            st.write(f"Koefisien Determinasi (R²): **{R2:.4f}**")

            # Gambar grafik
            fig, ax = plt.subplots()
            ax.scatter(x_vals, y_vals, label="Data Kalibrasi", color="blue")
            ax.plot(x_vals, y_fit, label=f"Regresi: y = {m:.2f}x + {b:.2f}", color="red")
            ax.axhline(y_sampel, color='green', linestyle='--', label=f"Abs Sampel = {y_sampel}")
            ax.axvline(x_sampel, color='orange', linestyle=':', label=f"x Sampel = {x_sampel:.2f}")
            ax.set_xlabel("Konsentrasi (x)")
            ax.set_ylabel("Absorbansi (y)")
            ax.set_title("Kurva Kalibrasi dan Absorbansi Sampel")
            ax.legend()
            st.pyplot(fig)

            # Hitung ketidakpastian diperluas
            if st.button("🎯 Hitung Ketidakpastian"):
                uc = mu_reg
                U = 2 * uc
                st.header("📤 Hasil Akhir")
                st.write(f"Ketidakpastian gabungan (uc): **{uc:.4f}**")
                st.write(f"Ketidakpastian diperluas (U, k=2): **{U:.4f}**")
                st.success(f"🔬 Konsentrasi Sampel: **{x_sampel:.2f} ± {U:.2f}** (95% CI)")
    except Exception as e:
        st.warning(f"Masukkan data numerik yang valid. Kesalahan: {e}")

# ==================== TAB 4 s.d. 6 =====================
with tab4:
    st.header("Ketidakpastian Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab5:
    st.header("Konversi Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab6:
    st.header("Titrasi Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
