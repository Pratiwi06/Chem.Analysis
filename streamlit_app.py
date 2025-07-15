import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Chemical Analysis App", layout="wide")

st.title("Chemical Analysis")
st.title("_chemical_ is :blue[cool] :sunglasses:")

# Buat tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Beranda", "Tabel Periodik", "Regresi", "Ketidakpastian", "Konversi", "Titrasi"])

# ==================== TAB 1 =====================
with tab1:
    st.header("📘 Selamat Datang di Aplikasi Analisis Kimia")
    st.write("Aplikasi ini dirancang untuk membantu analisis data kimia seperti regresi linear, konversi satuan, dan perhitungan titrasi.")

# ==================== TAB 2 =====================
with tab2:
    st.header("🔬 Tabel Periodik Interaktif")
    elements = [
           {"symbol": "Nb", "name": "Niobium", "atomicNumber": 41, "atomicMass": 92.90637, "electronConfiguration": "[Kr] 4d⁴ 5s²", "shells": 5},
    {"symbol": "Mo", "name": "Molybdenum", "atomicNumber": 42, "atomicMass": 95.95, "electronConfiguration": "[Kr] 4d⁵ 5s¹", "shells": 5},
    {"symbol": "Tc", "name": "Teknetium", "atomicNumber": 43, "atomicMass": 98, "electronConfiguration": "[Kr] 4d⁵ 5s²", "shells": 5},
    {"symbol": "Ru", "name": "Rutenium", "atomicNumber": 44, "atomicMass": 101.07, "electronConfiguration": "[Kr] 4d⁷ 5s¹", "shells": 5},
    {"symbol": "Rh", "name": "Rhodium", "atomicNumber": 45, "atomicMass": 102.90550, "electronConfiguration": "[Kr] 4d⁸ 5s¹", "shells": 5},
    {"symbol": "Pd", "name": "Palladium", "atomicNumber": 46, "atomicMass": 106.42, "electronConfiguration": "[Kr] 4d¹⁰", "shells": 5},
    {"symbol": "Ag", "name": "Perak", "atomicNumber": 47, "atomicMass": 107.8682, "electronConfiguration": "[Kr] 4d¹⁰ 5s¹", "shells": 5},
    {"symbol": "Cd", "name": "Kadmium", "atomicNumber": 48, "atomicMass": 112.414, "electronConfiguration": "[Kr] 4d¹⁰ 5s²", "shells": 5},
    {"symbol": "In", "name": "Indium", "atomicNumber": 49, "atomicMass": 114.818, "electronConfiguration": "[Kr] 4d¹⁰ 5s² 5p¹", "shells": 5},
    {"symbol": "Sn", "name": "Timah", "atomicNumber": 50, "atomicMass": 118.710, "electronConfiguration": "[Kr] 4d¹⁰ 5s² 5p²", "shells": 5},
    {"symbol": "Sb", "name": "Antimon", "atomicNumber": 51, "atomicMass": 121.760, "electronConfiguration": "[Kr] 4d¹⁰ 5s² 5p³", "shells": 5},
    {"symbol": "Te", "name": "Tellurium", "atomicNumber": 52, "atomicMass": 127.60, "electronConfiguration": "[Kr] 4d¹⁰ 5s² 5p⁴", "shells": 5},
    {"symbol": "I", "name": "Iodium", "atomicNumber": 53, "atomicMass": 126.90447, "electronConfiguration": "[Kr] 4d¹⁰ 5s² 5p⁵", "shells": 5},
    {"symbol": "Xe", "name": "Xenon", "atomicNumber": 54, "atomicMass": 131.293, "electronConfiguration": "[Kr] 4d¹⁰ 5s² 5p⁶", "shells": 5},
    {"symbol": "Cs", "name": "Cesium", "atomicNumber": 55, "atomicMass": 132.90545196, "electronConfiguration": "[Xe] 6s¹", "shells": 6},
    {"symbol": "Ba", "name": "Barium", "atomicNumber": 56, "atomicMass": 137.327, "electronConfiguration": "[Xe] 6s²", "shells": 6},
    {"symbol": "La", "name": "Lantanum", "atomicNumber": 57, "atomicMass": 138.90547, "electronConfiguration": "[Xe] 5d¹ 6s²", "shells": 6},
    {"symbol": "Ce", "name": "Cerium", "atomicNumber": 58, "atomicMass": 140.116, "electronConfiguration": "[Xe] 4f¹ 5d¹ 6s²", "shells": 6},
    {"symbol": "Pr", "name": "Praseodimium", "atomicNumber": 59, "atomicMass": 140.90766, "electronConfiguration": "[Xe] 4f³ 6s²", "shells": 6},
    {"symbol": "Nd", "name": "Neodimium", "atomicNumber": 60, "atomicMass": 144.242, "electronConfiguration": "[Xe] 4f⁴ 6s²", "shells": 6},
    {"symbol": "Pm", "name": "Prometium", "atomicNumber": 61, "atomicMass": 145, "electronConfiguration": "[Xe] 4f⁵ 6s²", "shells": 6},
    {"symbol": "Sm", "name": "Samarium", "atomicNumber": 62, "atomicMass": 150.36, "electronConfiguration": "[Xe] 4f⁶ 6s²", "shells": 6},
    {"symbol": "Eu", "name": "Eurium", "atomicNumber": 63, "atomicMass": 151.964, "electronConfiguration": "[Xe] 4f⁷ 6s²", "shells": 6},
    {"symbol": "Gd", "name": "Gadolinium", "atomicNumber": 64, "atomicMass": 157.25, "electronConfiguration": "[Xe] 4f⁷ 5d¹ 6s²", "shells": 6},
    {"symbol": "Tb", "name": "Terbium", "atomicNumber": 65, "atomicMass": 158.92535, "electronConfiguration": "[Xe] 4f⁹ 6s²", "shells": 6},
    {"symbol": "Dy", "name": "Dysprosium", "atomicNumber": 66, "atomicMass": 162.500, "electronConfiguration": "[Xe] 4f¹⁰ 6s²", "shells": 6},
    {"symbol": "Ho", "name": "Holmium", "atomicNumber": 67, "atomicMass": 164.93033, "electronConfiguration": "[Xe] 4f¹¹ 6s²", "shells": 6},
    {"symbol": "Er", "name": "Erbium", "atomicNumber": 68, "atomicMass": 167.259, "electronConfiguration": "[Xe] 4f¹² 6s²", "shells": 6},
    {"symbol": "Tm", "name": "Thulium", "atomicNumber": 69, "atomicMass": 168.93422, "electronConfiguration": "[Xe] 4f¹³ 6s²", "shells": 6},
    {"symbol": "Yb", "name": "Ytterbium", "atomicNumber": 70, "atomicMass": 173.04, "electronConfiguration": "[Xe] 4f¹⁴ 6s²", "shells": 6},
    {"symbol": "Lu", "name": "Lutecium", "atomicNumber": 71, "atomicMass": 174.9668, "electronConfiguration": "[Xe] 4f¹⁴ 5d¹ 6s²", "shells": 6},
    {"symbol": "Hf", "name": "Hafnium", "atomicNumber": 72, "atomicMass": 178.49, "electronConfiguration": "[Xe] 4f¹⁴ 5d² 6s²", "shells": 6},
    ]
    user_input = st.text_input("Masukkan nama unsur (contoh: Seng)").lower()
    found = False
    for elem in elements:
        if user_input == elem["name"].lower():
            st.success(f"Unsur: {elem['name']} ({elem['symbol']})")
            st.write(f"• Nomor Atom: {elem['atomicNumber']}")
            st.write(f"• Massa Atom: {elem['atomicMass']}")
            st.write(f"• Konfigurasi Elektron: {elem['electronConfiguration']}")
            st.write(f"• Kulit Elektron: {elem['shells']}")
            found = True
            break
    if user_input and not found:
        st.warning("Unsur tidak ditemukan dalam database.")

# ==================== TAB 3 =====================
with tab3:
    st.header(":bar_chart: Regresi Linear")

    x_input = st.text_input("Konsentrasi Standar (x), pisahkan koma", "")
    y_input = st.text_input("Absorbansi Standar (y), pisahkan koma", "")

    hitung = st.button("🔍 Hitung")

    if hitung and x_input and y_input:
        try:
            x_vals = np.array([float(v) for v in x_input.split(",")])
            y_vals = np.array([float(v) for v in y_input.split(",")])
            if len(x_vals) != len(y_vals):
                st.error("❌ Jumlah data x dan y tidak sama.")
            elif len(x_vals) < 2:
                st.warning("❗ Minimal 2 pasang data diperlukan.")
            else:
                n = len(x_vals)
                x_mean = np.mean(x_vals)
                y_mean = np.mean(y_vals)
                m = np.sum((x_vals - x_mean) * (y_vals - y_mean)) / np.sum((x_vals - x_mean) ** 2)
                b = y_mean - m * x_mean
                y_fit = m * x_vals + b
                Sy = np.sqrt(np.sum((y_vals - y_fit) ** 2) / (n - 2))
                r = np.corrcoef(x_vals, y_vals)[0, 1]
                R2 = r ** 2

                st.success(f"Persamaan regresi: y = {m:.4f}x + {b:.4f}")
                st.write(f"• Slope (m): {m:.4f}")
                st.write(f"• Intercept (b): {b:.4f}")
                st.write(f"Koefisien Korelasi (r): {r:.4f}")
                st.write(f"Koefisien Determinasi (R²): {R2:.4f}")

                RSD = Sy / y_mean * 100 if y_mean else 0.0
                st.success(f"%RSD Kurva Kalibrasi: {RSD:.2f}%")

                fig, ax = plt.subplots()
                ax.scatter(x_vals, y_vals, label='Data')
                ax.plot(x_vals, y_fit, color='red', label='Regresi')
                ax.set_xlabel('Konsentrasi')
                ax.set_ylabel('Absorbansi')
                ax.legend()
                st.pyplot(fig)

        except Exception as e:
            st.warning(f"❌ Masukkan data valid. Kesalahan: {e}")

# ==================== TAB 4 =====================
with tab4:
    st.header("Ketidakpastian Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

# ==================== TAB 5 =====================
with tab5:
    st.header("Konversi Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

# ==================== TAB 6 =====================
with tab6:
    st.header("Titrasi Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
