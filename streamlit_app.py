import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import streamlit.components.v1 as components

st.set_page_config(page_title="Chemical Analysis App", layout="wide")

st.title("Chemical Analysis")
st.title("_chemical_ is :blue[cool] :sunglasses:")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Beranda", "Tabel Periodik", "Regresi", "Ketidakpastian", "Konversi", "Titrasi"
])

# ==================== TAB 1 =====================
with tab1:
    st.header("Selamat datang di Aplikasi Analisis Kimia")
    st.write("Gunakan tab di atas untuk fitur analisis kimia.")

# ==================== TAB 2 =====================
with tab2:
    st.header("🔪 Tabel Periodik Interaktif")
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/01/Periodic_table_large.png", use_column_width=True)
    st.subheader("🔍 Cari Informasi Unsur")
    nama_unsur = st.text_input("Masukkan nama unsur (misal: oksigen)").lower().strip()
    elements = {
        "hidrogen": {"simbol": "H", "nomor_atom": 1, "massa_atom": 1.008},
        "helium": {"simbol": "He", "nomor_atom": 2, "massa_atom": 4.0026},
        "litium": {"simbol": "Li", "nomor_atom": 3, "massa_atom": 6.94},
        "berilium": {"simbol": "Be", "nomor_atom": 4, "massa_atom": 9.0122},
        "boron": {"simbol": "B", "nomor_atom": 5, "massa_atom": 10.81},
        "karbon": {"simbol": "C", "nomor_atom": 6, "massa_atom": 12.01},
        "nitrogen": {"simbol": "N", "nomor_atom": 7, "massa_atom": 14.01},
        "oksigen": {"simbol": "O", "nomor_atom": 8, "massa_atom": 16.00},
        "fluorin": {"simbol": "F", "nomor_atom": 9, "massa_atom": 19.00},
        "natrium": {"simbol": "Na", "nomor_atom": 11, "massa_atom": 22.99},
        "magnesium": {"simbol": "Mg", "nomor_atom": 12, "massa_atom": 24.31},
        "aluminium": {"simbol": "Al", "nomor_atom": 13, "massa_atom": 26.98},
        "silikon": {"simbol": "Si", "nomor_atom": 14, "massa_atom": 28.09},
        "klorin": {"simbol": "Cl", "nomor_atom": 17, "massa_atom": 35.45},
        "besi": {"simbol": "Fe", "nomor_atom": 26, "massa_atom": 55.85},
        "tembaga": {"simbol": "Cu", "nomor_atom": 29, "massa_atom": 63.55},
        "emas": {"simbol": "Au", "nomor_atom": 79, "massa_atom": 196.97},
    }
    if nama_unsur:
        if nama_unsur in elements:
            data = elements[nama_unsur]
            st.success(f"✅ {nama_unsur.capitalize()} ditemukan!")
            st.write(f"- **Simbol:** {data['simbol']}")
            st.write(f"- **Nomor Atom:** {data['nomor_atom']}")
            st.write(f"- **Massa Atom:** {data['massa_atom']} u")
        else:
            st.error("Unsur tidak ditemukan. Periksa ejaan dan coba lagi.")

# ==================== TAB 3 =====================
with tab3:
    st.header(":bar_chart: Regresi Linear dan Ketidakpastian Regresi")

    # Inisialisasi state
    for key, default in [("clear_state", False), ("has_calculated", False),
                         ("x_input", ""), ("y_input", ""), ("y_sampel", 0.0)]:
        if key not in st.session_state:
            st.session_state[key] = default

    if not st.session_state.clear_state:
        # Input data
        x_input = st.text_input("Konsentrasi Standar (x), pisahkan koma", st.session_state.x_input)
        y_input = st.text_input("Absorbansi Standar (y), pisahkan koma", st.session_state.y_input)
        y_sampel = st.number_input("Absorbansi Sampel", step=0.001, format="%.3f", value=st.session_state.y_sampel)
        # Simpan kembali ke state
        st.session_state.x_input = x_input
        st.session_state.y_input = y_input
        st.session_state.y_sampel = y_sampel
        # Tombol Hitung
        if not st.session_state.has_calculated and st.button("🔍 Hitung"):
            st.session_state.has_calculated = True
            st.experimental_rerun()
    else:
        # Mode clear: tampilkan tombol Kembali
        col1, col2 = st.columns([1, 1])
        _ = col1.empty()
        if col2.button("🔁 Kembali"):
            for key in ["clear_state", "has_calculated", "x_input", "y_input", "y_sampel"]:
                st.session_state[key] = False if isinstance(st.session_state[key], bool) else "" if isinstance(st.session_state[key], str) else 0.0
            st.experimental_rerun()

    # Proses perhitungan
    if st.session_state.has_calculated:
        if st.session_state.x_input.strip() and st.session_state.y_input.strip():
            try:
                x_vals = np.array([float(i) for i in st.session_state.x_input.split(",")])
                y_vals = np.array([float(i) for i in st.session_state.y_input.split(",")])
                if len(x_vals) != len(y_vals):
                    st.error("❌ Jumlah data x dan y tidak sama.")
                elif len(x_vals) < 2:
                    st.warning("❗ Minimal 2 pasang data diperlukan.")
                else:
                    n = len(x_vals)
                    x_mean = np.mean(x_vals)
                    y_mean = np.mean(y_vals)
                    # Regresi
                    m = np.sum((x_vals-x_mean)*(y_vals-y_mean))/np.sum((x_vals-x_mean)**2)
                    b = y_mean - m*x_mean
                    y_fit = m*x_vals + b
                    # Statistik
                    Sy = np.sqrt(np.sum((y_vals-y_fit)**2)/(n-2))
                    sum_sq_x = np.sum((x_vals-x_mean)**2)
                    # Hitung x_sampel dan mu_reg
                    x_sampel = (st.session_state.y_sampel - b)/m if m else 0
                    mu_reg = (Sy/m)*sqrt((1/n)+((x_sampel-x_mean)**2/sum_sq_x)) if m else 0
                    # Korelasi
                    r = np.corrcoef(x_vals,y_vals)[0,1]
                    R2 = r**2
                    # Tampilkan hasil
                    st.success(f"Persamaan regresi: y = {m:.4f}x + {b:.4f}")
                    st.write(f"• Slope (m): {m:.4f}")
                    st.write(f"• Intercept (b): {b:.4f}")
                    st.write(f"Koefisien Korelasi (r): {r:.4f}")
                    st.write(f"Koefisien Determinasi (R²): {R2:.4f}")
                    st.info(f"Hasil konsentrasi sampel = {x_sampel:.2f} ± {mu_reg:.2f} (μ_reg)")
                    # Grafik
                    fig, ax = plt.subplots()
                    ax.scatter(x_vals,y_vals,label='Data')
                    ax.plot(x_vals,y_fit,label='Regresi', color='red')
                    ax.set_xlabel('Konsentrasi')
                    ax.set_ylabel('Absorbansi')
                    ax.legend()
                    st.pyplot(fig)
                    # Ketidakpastian
                    U = 2*mu_reg
                    st.write(f"Ketidakpastian gabungan uc: {mu_reg:.4f}")
                    st.write(f"Ketidakpastian diperluas U: {U:.4f} (k=2)")
                    # Tombol Clear
                    if st.button("❌ Clear"):
                        st.session_state.clear_state = True
                        st.session_state.has_calculated = False
                        st.experimental_rerun()
            except Exception as e:
                st.warning(f"❌ Masukkan data valid. Kesalahan: {e}")
        else:
            st.info("⬅️ Masukkan data x dan y terlebih dahulu.")

# ==================== TAB 4 - 6 =====================
with tab4:
    st.header("Ketidakpastian Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
with tab5:
    st.header("Konversi Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
with tab6:
    st.header("Titrasi Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
