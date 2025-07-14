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
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/0/01/Periodic_table_large.png",
        use_column_width=True
    )
    st.subheader("🔍 Cari Informasi Unsur")
    nama_unsur = st.text_input("Masukkan nama unsur (misal: oksigen)").lower().strip()
    elements = {
        "oksigen": {"simbol": "O", "nomor_atom": 8, "massa_atom": 16.00},
        "hidrogen": {"simbol": "H", "nomor_atom": 1, "massa_atom": 1.008},
        # ... tambahkan unsur lain sesuai kebutuhan
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

    # Initialize session state
    for key, default in [("x_input", ""), ("y_input", ""), ("y_sampel", 0.0)]:
        if key not in st.session_state:
            st.session_state[key] = default

    # Input fields
    x_input = st.text_input("Konsentrasi Standar (x), pisahkan koma", st.session_state.x_input)
    y_input = st.text_input("Absorbansi Standar (y), pisahkan koma", st.session_state.y_input)
    y_sampel = st.number_input("Absorbansi Sampel", step=0.001, format="%.3f", value=st.session_state.y_sampel)
    st.session_state.x_input = x_input
    st.session_state.y_input = y_input
    st.session_state.y_sampel = y_sampel

        # Buttons side by side
    col1, col2 = st.columns(2)
    hitung = col1.button("🔍 Hitung")
    clear = col2.button("❌ Clear Input")

    # Clear action
    if clear:
        for k in ["x_input", "y_input", "y_sampel"]:
            st.session_state[k] = "" if isinstance(st.session_state[k], str) else 0.0
        hitung = False
    if clear:
        for k in ["x_input", "y_input", "y_sampel"]:
            st.session_state[k] = "" if isinstance(st.session_state[k], str) else 0.0
        hitung = False

    # Perform calculation
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
                m = np.sum((x_vals-x_mean)*(y_vals-y_mean))/np.sum((x_vals-x_mean)**2)
                b = y_mean - m*x_mean
                y_fit = m*x_vals + b
                Sy = np.sqrt(np.sum((y_vals-y_fit)**2)/(n-2))
                sum_sq_x = np.sum((x_vals-x_mean)**2)
                x_sampel = (y_sampel - b)/m if m else 0.0
                mu_reg = (Sy/m)*sqrt((1/n)+((x_sampel-x_mean)**2/sum_sq_x)) if m else 0.0
                r = np.corrcoef(x_vals,y_vals)[0,1]
                R2 = r**2

                st.success(f"Persamaan regresi: y = {m:.4f}x + {b:.4f}")
                st.write(f"• Slope (m): {m:.4f}")
                st.write(f"• Intercept (b): {b:.4f}")
                st.write(f"Koefisien Korelasi (r): {r:.4f}")
                st.write(f"Koefisien Determinasi (R²): {R2:.4f}")
                st.info(f"Ketidakpastian regresi (μ_reg): {mu_reg:.2f}")

                fig, ax = plt.subplots()
                ax.scatter(x_vals, y_vals, label='Data')
                ax.plot(x_vals, y_fit, color='red', label='Regresi')
                ax.set_xlabel('Konsentrasi')
                ax.set_ylabel('Absorbansi')
                ax.legend()
                st.pyplot(fig)

                U = 2 * mu_reg
                st.write(f"Ketidakpastian gabungan (uc): {mu_reg:.4f}")
                st.write(f"Ketidakpastian diperluas (U, k=2): {U:.4f}")
        except Exception as e:
            st.warning(f"❌ Masukkan data valid. Kesalahan: {e}")
    elif hitung:
        st.info("⬅️ Masukkan data x dan y terlebih dahulu untuk perhitungan.")

# ==================== TAB 4 - 6 ===================== - 6 =====================
with tab4:
    st.header("Ketidakpastian Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
with tab5:
    st.header("Konversi Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
with tab6:
    st.header("Titrasi Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
