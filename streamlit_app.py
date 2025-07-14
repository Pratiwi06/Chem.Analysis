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
    for key, default in [("x_input", ""), ("y_input", "")]:  # removed y_sampel state
        if key not in st.session_state:
            st.session_state[key] = default

    # Input fields
    x_input = st.text_input("Konsentrasi Standar (x), pisahkan koma", st.session_state.x_input)
    y_input = st.text_input("Absorbansi Standar (y), pisahkan koma", st.session_state.y_input)
    # Removed absorbansi sampel input
y_sampel = 0.0  # fixed default

        # Tombol Hitung
    hitung = st.button("🔍 Hitung")

    # Perform calculation when hitung pressed
    if hitung and x_input and y_input:
        y_sampel = 0.0  # using default

        st.info("⬅️ Masukkan data x dan y terlebih dahulu untuk perhitungan.")

# ==================== TAB 4 - 6 ===================== - 6 ===================== - 6 =====================
with tab4:
    st.header("Ketidakpastian Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
with tab5:
    st.header("Konversi Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
with tab6:
    st.header("Titrasi Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
