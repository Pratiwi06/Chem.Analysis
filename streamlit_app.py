import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(page_title="Chem Analysis", layout="wide")

# Sidebar sebagai navigasi utama
st.sidebar.title("🔬 Chem Analysis")
menu = st.sidebar.radio("Pilih Fitur:", ["Beranda", "Periodik Unsur", "Regresi Linier", "Konversi", "Standardisasi"])

st.markdown("""
    <style>
        .big-font {font-size:20px !important;}
        .title-text {font-size:32px; color:#4B8BBE; font-weight:bold;}
        .box {background-color:#f0f2f6; padding:20px; border-radius:10px;}
    </style>
""", unsafe_allow_html=True)

# ==================== BERANDA =====================
if menu == "Beranda":
    st.title("📘 Selamat Datang di Chem Analysis")
    st.markdown("""
    <div class='box'>
        <h1 class='title-text'>🧪 Aplikasi Analisis Kimia</h1>
        <h3>Selamat datang!</h3>
        <p>Aplikasi ini membantu kamu dalam:</p>
        <ul>
            <li>🔄 Konversi Satuan</li>
            <li>🧪 Titrasi / Standardisasi</li>
            <li>📊 Regresi Linear</li>
            <li>📘 Tabel Periodik</li>
        </ul>
        <p>Gunakan menu di samping untuk menjelajah fitur-fitur.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🎯 Tujuan Aplikasi")
    st.markdown("""
    Aplikasi ini dirancang untuk membantu analisis data kimia meliputi:
    - Tabel periodik unsur
    - Perhitungan regresi linear
    - Konversi satuan
    - Perhitungan standardisasi
    """)

    st.subheader("🌟 Manfaat Aplikasi")
    st.markdown("""
    - 💻 **Akses mudah** di berbagai platform
    - 🔍 **Mempermudah pembelajaran dan praktikum kimia**
    - 📈 **Mendukung pengolahan data laboratorium**
    - 🧠 **Memberikan pengalaman interaktif dan edukatif**
    """)

    st.subheader("🧰 Fitur-Fitur Tersedia")
    st.markdown("""
    ### 🧬 Tabel Periodik Unsur
    Informasi lengkap seperti simbol, nomor atom, massa atom, konfigurasi elektron, dll.

    ### 📊 Regresi Linear
    Hitung persamaan regresi, koefisien korelasi, R², dan lainnya.

    ### 🔄 Konversi Satuan
    Suhu, tekanan, volume, massa, dan konsentrasi.

    ### 🧪 Standardisasi Larutan
    Hitung konsentrasi berdasarkan titrasi berbagai metode.
    """)

    st.markdown("> 🚀 **Jelajahi fitur-fitur kami untuk pembelajaran kimia lebih seru!**")

# ==================== PERIODIK UNSUR =====================
elif menu == "Periodik Unsur":
    st.header("🔬 Periodik Unsur Kimia")
    # Kode sebelumnya ditaruh di sini (list unsur, selectbox, dll)
    st.info("🔧 Fitur ini dalam pengembangan.")

# ==================== REGRESI LINIER =====================
elif menu == "Regresi Linier":
    st.header("📈 Regresi Linier")

    x_input = st.text_input("Masukkan nilai X (pisahkan dengan koma)")
    y_input = st.text_input("Masukkan nilai Y (pisahkan dengan koma)")

    if st.button("🔍 Hitung"):
        try:
            x_vals = np.array([float(x) for x in x_input.split(",")])
            y_vals = np.array([float(y) for y in y_input.split(",")])

            if len(x_vals) != len(y_vals):
                st.error("Jumlah data X dan Y harus sama!")
            else:
                slope, intercept = np.polyfit(x_vals, y_vals, 1)
                r_value = np.corrcoef(x_vals, y_vals)[0,1]
                r_squared = r_value**2

                st.success("Hasil Regresi")
                st.write(f"Persamaan: y = {slope:.3f}x + {intercept:.3f}")
                st.write(f"Koefisien Korelasi (r): {r_value:.3f}")
                st.write(f"R²: {r_squared:.3f}")

                fig, ax = plt.subplots()
                ax.scatter(x_vals, y_vals, label='Data')
                ax.plot(x_vals, slope*x_vals + intercept, color='red', label='Regresi')
                ax.set_xlabel('X')
                ax.set_ylabel('Y')
                ax.legend()
                st.pyplot(fig)

        except ValueError:
            st.error("Input tidak valid. Gunakan angka dan pisahkan dengan koma.")

# ==================== KONVERSI =====================
elif menu == "Konversi":
    st.header("🔄 Konversi Satuan")
    st.info("🔧 Fitur ini dalam pengembangan.")

# ==================== STANDARDISASI =====================
elif menu == "Standardisasi":
    st.header("🧪 Standardisasi Larutan")
    st.info("🔧 Fitur ini dalam pengembangan.")
