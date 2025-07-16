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
    st.header("\U0001F4D8 Selamat Datang di Aplikasi Analisis Kimia")
    st.write("Aplikasi ini dirancang untuk membantu analisis data kimia seperti regresi linear, konversi satuan, dan perhitungan titrasi.")

# ==================== TAB 2 =====================
with tab2:
    st.header("\U0001F52C Tabel Periodik Interaktif")
    elements = [
        {"symbol": "Zn", "name": "Seng", "atomicNumber": 30, "atomicMass": 65.38, "electronConfiguration": "[Ar] 3d¹⁰ 4s²", "electronsPerShell": [2, 8, 18, 2]},
        {"symbol": "Ga", "name": "Galium", "atomicNumber": 31, "atomicMass": 69.723, "electronConfiguration": "[Ar] 3d¹⁰ 4s² 4p¹", "electronsPerShell": [2, 8, 18, 3]},
        {"symbol": "Ge", "name": "Germanium", "atomicNumber": 32, "atomicMass": 72.630, "electronConfiguration": "[Ar] 3d¹⁰ 4s² 4p²", "electronsPerShell": [2, 8, 18, 4]},
        {"symbol": "As", "name": "Arsen", "atomicNumber": 33, "atomicMass": 74.921595, "electronConfiguration": "[Ar] 3d¹⁰ 4s² 4p³", "electronsPerShell": [2, 8, 18, 5]},
        {"symbol": "Se", "name": "Selenium", "atomicNumber": 34, "atomicMass": 78.971, "electronConfiguration": "[Ar] 3d¹⁰ 4s² 4p⁴", "electronsPerShell": [2, 8, 18, 6]},
        {"symbol": "Br", "name": "Brom", "atomicNumber": 35, "atomicMass": 79.904, "electronConfiguration": "[Ar] 3d¹⁰ 4s² 4p⁵", "electronsPerShell": [2, 8, 18, 7]},
        {"symbol": "Kr", "name": "Kripton", "atomicNumber": 36, "atomicMass": 83.798, "electronConfiguration": "[Ar] 3d¹⁰ 4s² 4p⁶", "electronsPerShell": [2, 8, 18, 8]}
    ]
    user_input = st.text_input("Masukkan nama unsur (contoh: Seng)").lower()
    if user_input:
        found = False
        for elem in elements:
            if user_input == elem["name"].lower():
                st.success(f"Unsur: {elem['name']} ({elem['symbol']})")
                st.markdown(f"**Nomor Atom:** {elem['atomicNumber']}")
                st.markdown(f"**Massa Atom:** {elem['atomicMass']}")
                st.markdown(f"**Konfigurasi Elektron:** {elem['electronConfiguration']}")
                st.markdown(f"**Elektron tiap kulit:** {' - '.join(map(str, elem['electronsPerShell']))}")
                found = True
                break
        if not found:
            st.warning("Unsur tidak ditemukan dalam database.")

# ==================== TAB 3 =====================
with tab3:
    st.header(":bar_chart: Regresi Linear")

    x_input = st.text_input("Nilai X (x), pisahkan koma", "")
    y_input = st.text_input("Nilai Y (y), pisahkan koma", "")

    hitung = st.button("\U0001F50D Hitung")

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
    st.header("\U0001F9EA Perhitungan Titrasi Kimia")
    st.markdown("Masukkan data titrasi duplo untuk menghitung **Normalitas Sampel, Rata-rata, SD**, dan **%RPD**.")

    # Pilih jenis titrasi
    jenis_titrasi = st.selectbox("Pilih Jenis Titrasi", [
        "Asam-Basa", "Argentometri", "Kompleksiometri", "Permanganometri"
    ])

    # Input data
    col1, col2 = st.columns(2)
    with col1:
        V1 = st.number_input("Volume Titrasi ke-1 (mL)", min_value=0.0, step=0.01, format="%.2f")
        N_titran = st.number_input("Normalitas Titran", min_value=0.0001, step=0.0001, format="%.4f")
    with col2:
        V2 = st.number_input("Volume Titrasi ke-2 (mL)", min_value=0.0, step=0.01, format="%.2f")
        V_sampel = st.number_input("Volume Sampel (mL)", min_value=0.01, step=0.01, format="%.2f")

    if st.button("Hitung Titrasi"):
        volumes = np.array([V1, V2])
        avg_V = np.mean(volumes)
        std_V = np.std(volumes, ddof=1) if len(volumes) > 1 else 0
        rpd = (abs(V1 - V2) / avg_V) * 100 if avg_V != 0 else 0
        N_sampel = (N_titran * avg_V) / V_sampel if V_sampel != 0 else 0

        st.subheader("\U0001F4CA Hasil Perhitungan Titrasi")
        st.write(f"**Jenis Titrasi:** {jenis_titrasi}")
        st.write(f"**Rata-rata Volume Titrasi:** {avg_V:.2f} mL")
        st.write(f"**Standar Deviasi (SD):** {std_V:.4f}")
        st.write(f"**%RPD:** {rpd:.2f}%")
        st.success(f"**Normalitas Sampel:** {N_sampel:.4f} N")
