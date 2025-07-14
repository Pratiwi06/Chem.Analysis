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
    st.write("Silakan pilih tab untuk mulai menggunakan fitur analisis.")

# ==================== TAB 2 =====================
with tab2:
    st.header("Tabel Periodik")
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/01/Periodic_table_large.png", use_column_width=True)

# ==================== TAB 3 - REGRESI =====================
with tab3:
    st.header("📊 Regresi Linear dan Ketidakpastian dari Kalibrasi")

    with st.expander("📈 Input Data Kurva Kalibrasi"):
        x_kal = st.text_input("Konsentrasi Standar (x), pisahkan koma", "2, 4, 6, 8, 10")
        y_kal = st.text_input("Absorbansi Standar (y), pisahkan koma", "0.145, 0.289, 0.429, 0.565, 0.712")
        y_sampel = st.number_input("Absorbansi Sampel", value=0.400, step=0.
