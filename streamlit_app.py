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
           {"symbol": "Li", "name": "Litium", "atomicNumber": 3, "atomicMass": 6.941, "electronConfiguration": "[He] 2s¹", "electronsPerShell": [2, 1]},
    {"symbol": "Be", "name": "Berilium", "atomicNumber": 4, "atomicMass": 9.012182, "electronConfiguration": "[He] 2s²", "electronsPerShell": [2, 2]},
    {"symbol": "B", "name": "Bor", "atomicNumber": 5, "atomicMass": 10.811, "electronConfiguration": "[He] 2s² 2p¹", "electronsPerShell": [2, 3]},
    {"symbol": "C", "name": "Karbon", "atomicNumber": 6, "atomicMass": 12.0107, "electronConfiguration": "[He] 2s² 2p²", "electronsPerShell": [2, 4]},
    {"symbol": "N", "name": "Nitrogen", "atomicNumber": 7, "atomicMass": 14.0067, "electronConfiguration": "[He] 2s² 2p³", "electronsPerShell": [2, 5]},
    {"symbol": "O", "name": "Oksigen", "atomicNumber": 8, "atomicMass": 15.9994, "electronConfiguration": "[He] 2s² 2p⁴", "electronsPerShell": [2, 6]},
    {"symbol": "F", "name": "Fluorin", "atomicNumber": 9, "atomicMass": 18.9984032, "electronConfiguration": "[He] 2s² 2p⁵", "electronsPerShell": [2, 7]},
    {"symbol": "Ne", "name": "Neon", "atomicNumber": 10, "atomicMass": 20.1797, "electronConfiguration": "[He] 2s² 2p⁶", "electronsPerShell": [2, 8]},
    {"symbol": "Na", "name": "Natrium", "atomicNumber": 11, "atomicMass": 22.98976928, "electronConfiguration": "[Ne] 3s¹", "electronsPerShell": [2, 8, 1]},
    {"symbol": "Mg", "name": "Magnesium", "atomicNumber": 12, "atomicMass": 24.305, "electronConfiguration": "[Ne] 3s²", "electronsPerShell": [2, 8, 2]},
    {"symbol": "Al", "name": "Alumunium", "atomicNumber": 13, "atomicMass": 26.9815386, "electronConfiguration": "[Ne] 3s² 3p¹", "electronsPerShell": [2, 8, 3]},
    {"symbol": "Si", "name": "Silikon", "atomicNumber": 14, "atomicMass": 28.0855, "electronConfiguration": "[Ne] 3s² 3p²", "electronsPerShell": [2, 8, 4]},
    {"symbol": "P", "name": "Fosfor", "atomicNumber": 15, "atomicMass": 30.973762, "electronConfiguration": "[Ne] 3s² 3p³", "electronsPerShell": [2, 8, 5]},
    {"symbol": "S", "name": "Belerang", "atomicNumber": 16, "atomicMass": 32.065, "electronConfiguration": "[Ne] 3s² 3p⁴", "electronsPerShell": [2, 8, 6]},
    {"symbol": "Cl", "name": "Klor", "atomicNumber": 17, "atomicMass": 35.453, "electronConfiguration": "[Ne] 3s² 3p⁵", "electronsPerShell": [2, 8, 7]},
    {"symbol": "Ar", "name": "Argon", "atomicNumber": 18, "atomicMass": 39.948, "electronConfiguration": "[Ne] 3s² 3p⁶", "electronsPerShell": [2, 8, 8]},
    {"symbol": "K", "name": "Kalium", "atomicNumber": 19, "atomicMass": 39.0983, "electronConfiguration": "[Ar] 4s¹", "electronsPerShell": [2, 8, 8, 1]},
    {"symbol": "Ca", "name": "Kalsium", "atomicNumber": 20, "atomicMass": 40.078, "electronConfiguration": "[Ar] 4s²", "electronsPerShell": [2, 8, 8, 2]},
    {"symbol": "Sc", "name": "Skandium", "atomicNumber": 21, "atomicMass": 44.955908, "electronConfiguration": "[Ar] 3d¹ 4s²", "electronsPerShell": [2, 8, 8, 3]},
    {"symbol": "Ti", "name": "Titanium", "atomicNumber": 22, "atomicMass": 47.867, "electronConfiguration": "[Ar] 3d² 4s²", "electronsPerShell": [2, 8, 8, 4]},
    {"symbol": "V", "name": "Vanadium", "atomicNumber": 23, "atomicMass": 50.9415, "electronConfiguration": "[Ar] 3d³ 4s²", "electronsPerShell": [2, 8, 8, 5]},
    {"symbol": "Cr", "name": "Krom", "atomicNumber": 24, "atomicMass": 51.9961, "electronConfiguration": "[Ar] 3d⁵ 4s¹", "electronsPerShell": [2, 8, 8, 6]},
    {"symbol": "Mn", "name": "Mangan", "atomicNumber": 25, "atomicMass": 54.938044, "electronConfiguration": "[Ar] 3d⁵ 4s²", "electronsPerShell": [2, 8, 8, 7]},
    {"symbol": "Fe", "name": "Besi", "atomicNumber": 26, "atomicMass": 55.845, "electronConfiguration": "[Ar] 3d⁶ 4s²", "electronsPerShell": [2, 8, 8, 8]},
    {"symbol": "Co", "name": "Kobalt", "atomicNumber": 27, "atomicMass": 58.933194, "electronConfiguration": "[Ar] 3d⁷ 4s²", "electronsPerShell": [2, 8, 8, 9]},
    {"symbol": "Ni", "name": "Nikel", "atomicNumber": 28, "atomicMass": 58.6934, "electronConfiguration": "[Ar] 3d⁸ 4s²", "electronsPerShell": [2, 8, 8, 10]},
    {"symbol": "Cu", "name": "Tembaga", "atomicNumber": 29, "atomicMass": 63.546, "electronConfiguration": "[Ar] 3d¹⁰ 4s¹", "electronsPerShell": [2, 8, 8, 11]},
    {"symbol": "Zn", "name": "Seng", "atomicNumber": 30, "atomicMass": 65.38, "electronConfiguration": "[Ar] 3d¹⁰ 4s²", "electronsPerShell": [2, 8, 8, 12]},
    {"symbol": "Ga", "name": "Galium", "atomicNumber": 31, "atomicMass": 69.723, "electronConfiguration": "[Ar] 3d¹⁰ 4s² 4p¹", "electronsPerShell": [2, 8, 8, 13]},
    {"symbol": "Ge", "name": "Germanium", "atomicNumber": 32, "atomicMass": 72.630, "electronConfiguration": "[Ar] 3d¹⁰ 4s² 4p²", "electronsPerShell": [2, 8, 8, 14]},
    {"symbol": "As", "name": "Arsen", "atomicNumber": 33, "atomicMass": 74.921595, "electronConfiguration": "[Ar] 3d¹⁰ 4s² 4p³", "electronsPerShell": [2, 8, 8, 15]},
    {"symbol": "Se", "name": "Selenium", "atomicNumber": 34, "atomicMass": 78.971, "electronConfiguration": "[Ar] 3d¹⁰ 4s² 4p⁴", "electronsPerShell": [2, 8, 8, 16]},
    user_input = st.text_input("Masukkan nama unsur (contoh: Seng)").lower()
    found = False
    for elem in elements:
        if user_input == elem["name"].lower():
            st.success(f"Unsur: {elem['name']} ({elem['symbol']})")
            st.write(f"• Nomor Atom: {elem['atomicNumber']}")
            st.write(f"• Massa Atom: {elem['atomicMass']}")
            st.write(f"• Konfigurasi Elektron: {elem['electronConfiguration']}")
            st.write(f"• Elektron tiap kulit: {elem['electronsPerShell']}")
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
