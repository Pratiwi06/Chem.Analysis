import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi halaman
def set_custom_background(image_url):
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.60), rgba(0,0,0,0.60)), 
                        url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """, unsafe_allow_html=True)

image_link = "https://i.pinimg.com/736x/d4/4a/4f/d44a4fc2f4d3a6a0c9a847088c059cd6.jpg"
set_custom_background(image_link)
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
    st.markdown("""
        <style>
            .welcome-box {
                background-color: #e6f7ff;
                padding: 25px;
                border-radius: 15px;
                border: 1px solid #91d5ff;
                margin-bottom: 25px;
                color: #000000; /* Warna teks hitam */
            }
            .section-box {
                background-color: #e6f7ff;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 20px;
                box-shadow: 0 2px 6px rgba(0,0,0,0.05);
                color: #000000; /* Warna teks hitam */
            }
            ul li {
                margin-bottom: 6px;
                font-size: 16px;
            }
            h3, h2 {
                color: #096dd9;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h1 style='text-align: center; font-size: 40px;'>🧪 Chem Analysis </h1>
    <h3 style='text-align: center; font-size: 20px; color: gray;'> 🌟Selamat Datang di Aplikasi Analisis Kimia🌟</h3>
    """, unsafe_allow_html=True)

        # Tambahan untuk nama kelompok
    with st.expander("👥 Kelompok 1- ANKIM 1A - Politeknik AKA Bogor"):
        st.markdown("""
        **Anggota:**
        - Abdillah Hafiz Xavier
        - Delia Pratiwi
        - Maulana Aziz  Asfin
        - Nayla Aulia Fitryani
        - Salma Seftia Darmawan
        """)
    st.markdown("""

    Gunakan menu di sebelah kiri untuk menjelajah fitur-fitur yang tersedia.
    """)

   

    st.markdown("""
        <div class='section-box'>
            <h3>🎯 Tujuan Aplikasi</h3>
            <p>
                Aplikasi ini dirancang untuk membantu analisis data kimia meliputi:
                <ul>
                    <li>📘 Tabel periodik unsur</li>
                    <li>📊 Perhitungan regresi linear</li>
                    <li>🔄 Konversi satuan</li>
                    <li>🧪 Perhitungan standardisasi larutan</li>
                </ul>
            </p>
        </div>

        <div class='section-box'>
            <h3>📘 Manfaat Aplikasi</h3>
            <ul>
                <li>💻 <b>Akses mudah</b> di berbagai platform</li>
                <li>🔍 <b>Mempermudah pembelajaran dan praktikum kimia</b></li>
                <li>📈 <b>Mendukung pengolahan data laboratorium</b></li>
                <li>🧠 <b>Memberikan pengalaman interaktif dan edukatif</b></li>
            </ul>
        </div>

        <div class='section-box'>
            <h3>🧰 Fitur-Fitur Tersedia</h3>
            <ul>
                <li><b>🧬 Tabel Periodik Unsur</b><br>Informasi lengkap seperti simbol, nomor atom, massa atom, konfigurasi elektron, dll.</li>
                <li><b>📊 Regresi Linear</b><br>Hitung persamaan regresi, koefisien korelasi, R², dan lainnya.</li>
                <li><b>🔄 Konversi Satuan</b><br>Suhu, tekanan, volume, massa, dan konsentrasi.</li>
                <li><b>🧪 Standardisasi Larutan</b><br>Hitung konsentrasi berdasarkan titrasi berbagai metode.</li>
            </ul>
        </div>

        <blockquote>🚀 <b>Jelajahi fitur-fitur kami untuk pembelajaran kimia lebih seru!</b></blockquote>
    """, unsafe_allow_html=True)


# ==================== PERIODIK UNSUR =====================
elif menu == "Periodik Unsur":
    st.header("🔬 Periodik Unsur Kimia")
    elements = [
        {"symbol": "H", "name": "Hidrogen", "atomicNumber": 1, "atomicMass": 1.00794, "electronConfiguration": "1s¹", "electronsPerShell": [1]},
        {"symbol": "He", "name": "Helium", "atomicNumber": 2, "atomicMass": 4.002602, "electronConfiguration": "1s²", "electronsPerShell": [2]},
        {"symbol": "Li", "name": "Litium", "atomicNumber": 3, "atomicMass": 6.941, "electronConfiguration": "[He] 2s¹", "electronsPerShell": [2, 1]},
        {"symbol": "Be", "name": "Berilium", "atomicNumber": 4, "atomicMass": 9.012182, "electronConfiguration": "[He] 2s²", "electronsPerShell": [2, 2]},
        {"symbol": "B", "name": "Boron", "atomicNumber": 5, "atomicMass": 10.811, "electronConfiguration": "[He] 2s² 2p¹", "electronsPerShell": [2, 3]},
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
        {"symbol": "Br", "name": "Brom", "atomicNumber": 35, "atomicMass": 79.904, "electronConfiguration": "[Ar] 3d¹⁰ 4s² 4p⁵", "electronsPerShell": [2, 8, 8, 17]},
        {"symbol": "Kr", "name": "Kripton", "atomicNumber": 36, "atomicMass": 83.798, "electronConfiguration": "[Ar] 3d¹⁰ 4s² 4p⁶", "electronsPerShell": [2, 8, 8, 18]},
        {"symbol": "Rb", "name": "Rubidium", "atomicNumber": 37, "atomicMass": 85.4678, "electronConfiguration": "[Kr] 5s¹", "electronsPerShell": [2, 8, 8, 18, 1]},
        {"symbol": "Sr", "name": "Strontium", "atomicNumber": 38, "atomicMass": 87.621, "electronConfiguration": "[Kr] 5s²", "electronsPerShell": [2, 8, 8, 18, 2]},
        {"symbol": "Y", "name": "Yttrium", "atomicNumber": 39, "atomicMass": 88.90585, "electronConfiguration": "[Kr] 4d¹ 5s²", "electronsPerShell": [2, 8, 8, 18, 3]},
        {"symbol": "Zr", "name": "Zirkonium", "atomicNumber": 40, "atomicMass": 91.224, "electronConfiguration": "[Kr] 4d² 5s²", "electronsPerShell": [2, 8, 8, 18, 4]},
        {"symbol": "Nb", "name": "Niobium", "atomicNumber": 41, "atomicMass": 92.90637, "electronConfiguration": "[Kr] 4d⁴ 5s²", "electronsPerShell": [2, 8, 8, 18, 5]},
        {"symbol": "Mo", "name": "Molybdenum", "atomicNumber": 42, "atomicMass": 95.95, "electronConfiguration": "[Kr] 4d⁵ 5s¹", "electronsPerShell": [2, 8, 8, 18, 6]},
        {"symbol": "Tc", "name": "Teknetium", "atomicNumber": 43, "atomicMass": 98, "electronConfiguration": "[Kr] 4d⁵ 5s²", "electronsPerShell": [2, 8, 8, 18, 7]},
        {"symbol": "Ru", "name": "Rutenium", "atomicNumber": 44, "atomicMass": 101.07, "electronConfiguration": "[Kr] 4d⁷ 5s¹", "electronsPerShell": [2, 8, 8, 18, 8]},
        {"symbol": "Rh", "name": "Rhodium", "atomicNumber": 45, "atomicMass": 102.90550, "electronConfiguration": "[Kr] 4d⁸ 5s¹", "electronsPerShell": [2, 8, 8, 18, 9]},
        {"symbol": "Pd", "name": "Palladium", "atomicNumber": 46, "atomicMass": 106.42, "electronConfiguration": "[Kr] 4d¹⁰", "electronsPerShell": [2, 8, 8, 18, 10]},
        {"symbol": "Ag", "name": "Perak", "atomicNumber": 47, "atomicMass": 107.8682, "electronConfiguration": "[Kr] 4d¹⁰ 5s¹", "electronsPerShell": [2, 8, 8, 18, 11]},
        {"symbol": "Cd", "name": "Kadmium", "atomicNumber": 48, "atomicMass": 112.414, "electronConfiguration": "[Kr] 4d¹⁰ 5s²", "electronsPerShell": [2, 8, 8, 18, 12]},
        {"symbol": "In", "name": "Indium", "atomicNumber": 49, "atomicMass": 114.818, "electronConfiguration": "[Kr] 4d¹⁰ 5s² 5p¹", "electronsPerShell": [2, 8, 8, 18, 13]},
        {"symbol": "Sn", "name": "Timah", "atomicNumber": 50, "atomicMass": 118.710, "electronConfiguration": "[Kr] 4d¹⁰ 5s² 5p²", "electronsPerShell": [2, 8, 8, 18, 14]},
        {"symbol": "Sb", "name": "Antimon", "atomicNumber": 51, "atomicMass": 121.760, "electronConfiguration": "[Kr] 4d¹⁰ 5s² 5p³", "electronsPerShell": [2, 8, 8, 18, 15]},
        {"symbol": "Te", "name": "Tellurium", "atomicNumber": 52, "atomicMass": 127.60, "electronConfiguration": "[Kr] 4d¹⁰ 5s² 5p⁴", "electronsPerShell": [2, 8, 8, 18, 16]},
        {"symbol": "I", "name": "Iodium", "atomicNumber": 53, "atomicMass": 126.90447, "electronConfiguration": "[Kr] 4d¹⁰ 5s² 5p⁵", "electronsPerShell": [2, 8, 8, 18, 17]},
        {"symbol": "Xe", "name": "Xenon", "atomicNumber": 54, "atomicMass": 131.293, "electronConfiguration": "[Kr] 4d¹⁰ 5s² 5p⁶", "electronsPerShell": [2, 8, 8, 18, 18]},
        {"symbol": "Cs", "name": "Cesium", "atomicNumber": 55, "atomicMass": 132.90545196, "electronConfiguration": "[Xe] 6s¹", "electronsPerShell": [2, 8, 8, 18, 18, 1]},
        {"symbol": "Ba", "name": "Barium", "atomicNumber": 56, "atomicMass": 137.327, "electronConfiguration": "[Xe] 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 2]},
        {"symbol": "La", "name": "Lantanum", "atomicNumber": 57, "atomicMass": 138.90547, "electronConfiguration": "[Xe] 5d¹ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 3]},
        {"symbol": "Ce", "name": "Cerium", "atomicNumber": 58, "atomicMass": 140.116, "electronConfiguration": "[Xe] 4f¹ 5d¹ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 4]},
        {"symbol": "Pr", "name": "Praseodimium", "atomicNumber": 59, "atomicMass": 140.90766, "electronConfiguration": "[Xe] 4f³ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 5]},
        {"symbol": "Nd", "name": "Neodimium", "atomicNumber": 60, "atomicMass": 144.242, "electronConfiguration": "[Xe] 4f⁴ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 6]},
        {"symbol": "Pm", "name": "Prometium", "atomicNumber": 61, "atomicMass": 145, "electronConfiguration": "[Xe] 4f⁵ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 7]},
        {"symbol": "Sm", "name": "Samarium", "atomicNumber": 62, "atomicMass": 150.36, "electronConfiguration": "[Xe] 4f⁶ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 8]},
        {"symbol": "Eu", "name": "Eurium", "atomicNumber": 63, "atomicMass": 151.964, "electronConfiguration": "[Xe] 4f⁷ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 9]},
        {"symbol": "Gd", "name": "Gadolinium", "atomicNumber": 64, "atomicMass": 157.25, "electronConfiguration": "[Xe] 4f⁷ 5d¹ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 10]},
        {"symbol": "Tb", "name": "Terbium", "atomicNumber": 65, "atomicMass": 158.92535, "electronConfiguration": "[Xe] 4f⁹ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 11]},
        {"symbol": "Dy", "name": "Dysprosium", "atomicNumber": 66, "atomicMass": 162.500, "electronConfiguration": "[Xe] 4f¹⁰ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 12]},
        {"symbol": "Ho", "name": "Holmium", "atomicNumber": 67, "atomicMass": 164.93033, "electronConfiguration": "[Xe] 4f¹¹ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 13]},
        {"symbol": "Er", "name": "Erbium", "atomicNumber": 68, "atomicMass": 167.259, "electronConfiguration": "[Xe] 4f¹² 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 14]},
        {"symbol": "Tm", "name": "Thulium", "atomicNumber": 69, "atomicMass": 168.93422, "electronConfiguration": "[Xe] 4f¹³ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 15]},
        {"symbol": "Yb", "name": "Ytterbium", "atomicNumber": 70, "atomicMass": 173.04, "electronConfiguration": "[Xe] 4f¹⁴ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 16]},
        {"symbol": "Lu", "name": "Lutecium", "atomicNumber": 71, "atomicMass": 174.9668, "electronConfiguration": "[Xe] 4f¹⁴ 5d¹ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 17]},
        {"symbol": "Hf", "name": "Hafnium", "atomicNumber": 72, "atomicMass": 178.49, "electronConfiguration": "[Xe] 4f¹⁴ 5d² 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 18]},
        {"symbol": "Ta", "name": "Tantalum", "atomicNumber": 73, "atomicMass": 180.94788, "electronConfiguration": "[Xe] 4f¹⁴ 5d³ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 19]},
        {"symbol": "W", "name": "Wolfram", "atomicNumber": 74, "atomicMass": 183.84, "electronConfiguration": "[Xe] 4f¹⁴ 5d⁴ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 20]},
        {"symbol": "Re", "name": "Rhenium", "atomicNumber": 75, "atomicMass": 186.207, "electronConfiguration": "[Xe] 4f¹⁴ 5d⁵ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 21]},
        {"symbol": "Os", "name": "Osmium", "atomicNumber": 76, "atomicMass": 190.23, "electronConfiguration": "[Xe] 4f¹⁴ 5d⁶ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 22]},
        {"symbol": "Ir", "name": "Iridium", "atomicNumber": 77, "atomicMass": 192.217, "electronConfiguration": "[Xe] 4f¹⁴ 5d⁷ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 23]},
        {"symbol": "Pt", "name": "Platina", "atomicNumber": 78, "atomicMass": 195.084, "electronConfiguration": "[Xe] 4f¹⁴ 5d⁸ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 24]},
        {"symbol": "Au", "name": "Emas", "atomicNumber": 79, "atomicMass": 196.966569, "electronConfiguration": "[Xe] 4f¹⁴ 5d⁹ 6s¹", "electronsPerShell": [2, 8, 8, 18, 18, 25]},
        {"symbol": "Hg", "name": "Merkuri", "atomicNumber": 80, "atomicMass": 200.592, "electronConfiguration": "[Xe] 4f¹⁴ 5d¹⁰ 6s²", "electronsPerShell": [2, 8, 8, 18, 18, 26]},
        {"symbol": "Tl", "name": "Tali", "atomicNumber": 81, "atomicMass": 204.38, "electronConfiguration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p¹", "electronsPerShell": [2, 8, 8, 18, 18, 27]},
        {"symbol": "Pb", "name": "Timbal", "atomicNumber": 82, "atomicMass": 207.2, "electronConfiguration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p²", "electronsPerShell": [2, 8, 8, 18, 18, 28]},
        {"symbol": "Bi", "name": "Bismut", "atomicNumber": 83, "atomicMass": 208.98040, "electronConfiguration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p³", "electronsPerShell": [2, 8, 8, 18, 18, 29]},
        {"symbol": "Po", "name": "Polonium", "atomicNumber": 84, "atomicMass": 209, "electronConfiguration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁴", "electronsPerShell": [2, 8, 8, 18, 18, 30]},
        {"symbol": "At", "name": "Astatin", "atomicNumber": 85, "atomicMass": 210, "electronConfiguration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁵", "electronsPerShell": [2, 8, 8, 18, 18, 31]},
        {"symbol": "Rn", "name": "Radon", "atomicNumber": 86, "atomicMass": 222, "electronConfiguration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁶", "electronsPerShell": [2, 8, 8, 18, 18, 32]},
        {"symbol": "Fr", "name": "Fransium", "atomicNumber": 87, "atomicMass": 223, "electronConfiguration": "[Rn] 7s¹", "electronsPerShell": [2, 8, 8, 18, 18, 32, 1]},
        {"symbol": "Ra", "name": "Radium", "atomicNumber": 88, "atomicMass": 226, "electronConfiguration": "[Rn] 7s²", "electronsPerShell": [2, 8, 8, 18, 18, 32, 2]},
        {"symbol": "Ac", "name": "Aktinium", "atomicNumber": 89, "atomicMass": 227, "electronConfiguration": "[Rn] 6d¹ 7s²", "electronsPerShell": [2, 8, 8, 18, 18, 32, 3]},
        {"symbol": "Th", "name": "Torium", "atomicNumber": 90, "atomicMass": 232.038, "electronConfiguration": "[Rn] 6d² 7s²", "electronsPerShell": [2, 8, 8, 18, 18, 32, 4]},
        {"symbol": "Pa", "name": "Protaktinium", "atomicNumber": 91, "atomicMass": 231.03588, "electronConfiguration": "[Rn] 5f² 7s²", "electronsPerShell": [2, 8, 8, 18, 18, 32, 5]},
        {"symbol": "U", "name": "Uranium", "atomicNumber": 92, "atomicMass": 238.02891, "electronConfiguration": "[Rn] 5f³ 7s²", "electronsPerShell": [2, 8, 8, 18, 18, 32, 6]},
        {"symbol": "Np", "name": "Neptunium", "atomicNumber": 93, "atomicMass": 237, "electronConfiguration": "[Rn] 5f⁴ 7s²", "electronsPerShell": [2, 8, 8, 18, 18, 32, 7]},
        {"symbol": "Pu", "name": "Plutonium", "atomicNumber": 94, "atomicMass": 244, "electronConfiguration": "[Rn] 5f⁶ 7s²", "electronsPerShell": [2, 8, 8, 18, 18, 32, 8]},
        {"symbol": "Am", "name": "Amerisium", "atomicNumber": 95, "atomicMass": 243, "electronConfiguration": "[Rn] 5f⁷ 7s²", "electronsPerShell": [2, 8, 8, 18, 18, 32, 9]},
        {"symbol": "Cm", "name": "Curium", "atomicNumber": 96, "atomicMass": 247, "electronConfiguration": "[Rn] 5f⁷ 7s²", "electronsPerShell": [2, 8, 8, 18, 18, 32, 10]},
        {"symbol": "Bk", "name": "Berkelium", "atomicNumber": 97, "atomicMass": 247, "electronConfiguration": "[Rn] 5f⁹ 7s²", "electronsPerShell": [2, 8, 8, 18, 18, 32, 11]},
        {"symbol": "Cf", "name": "Kalifornium", "atomicNumber": 98, "atomicMass": 251, "electronConfiguration": "[Rn] 5f¹⁰ 7s²", "electronsPerShell": [2, 8, 8, 18, 18, 32, 12]},
        {"symbol": "Es", "name": "Einsteinium", "atomicNumber": 99, "atomicMass": 252, "electronConfiguration": "[Rn] 5f¹¹ 7s²", "electronsPerShell": [2, 8, 8, 18, 18, 32, 13]},
        {"symbol": "Fm", "name": "Fermium", "atomicNumber": 100, "atomicMass": 257, "electronConfiguration": "[Rn] 5f¹² 7s²", "electronsPerShell": [2, 8, 8, 18, 18, 32, 14]},
        {"symbol": "Md", "name": "Mendelevium", "atomicNumber": 101, "atomicMass": 258, "electronConfiguration": "[Rn] 5f¹³ 7s²", "electronsPerShell": [2, 8, 8, 18, 18, 32, 15]},
        {"symbol": "No", "name": "Nobelium", "atomicNumber": 102, "atomicMass": 259, "electronConfiguration": "[Rn] 5f¹⁴ 7s²", "electronsPerShell": [2, 8, 8, 18, 18, 32, 16]},
        {"symbol": "Lr", "name": "Lawrencium", "atomicNumber": 103, "atomicMass": 262, "electronConfiguration": "[Rn] 5f¹⁴ 7s² 7p¹", "electronsPerShell": [2, 8, 8, 18, 18, 32, 17]},
    ]
        # Nama unsur untuk dropdown
    element_names = [""] + [elem["name"] for elem in elements]  # "" untuk default kosong

    # Pilihan pengguna
    selected_name = st.selectbox("🔍 Ketik atau pilih nama unsur:", element_names)

    if selected_name != "":
        for elem in elements:
            if elem["name"] == selected_name:
                st.success(f"Unsur: {elem['name']} ({elem['symbol']})")
                st.markdown(f"**Nomor Atom:** {elem['atomicNumber']}")
                st.markdown(f"**Massa Atom:** {elem['atomicMass']}")
                st.markdown(f"**Konfigurasi Elektron:** {elem['electronConfiguration']}")
                st.markdown(f"**Elektron tiap kulit:** {' - '.join(map(str, elem['electronsPerShell']))}")
                break


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
    st.header("Konversi Satuan")
    conversion_type = st.selectbox("Pilih jenis konversi:", ["Suhu", "Tekanan", "Volume", "Massa", "Konsentrasi"])

    if conversion_type == "Suhu":
        st.subheader("Konversi Suhu")
        temp_value = st.number_input("Masukkan nilai suhu:")
        temp_unit = st.selectbox("Pilih satuan suhu:", ["Celsius", "Fahrenheit", "Kelvin", "Reamur"])

        if st.button("Konversi"):
            if temp_unit == "Celsius":
                fahrenheit = (temp_value * 9/5) + 32
                kelvin = temp_value + 273.15
                reamur = temp_value * 4/5
                st.success(f"{temp_value} °C = {fahrenheit:.1f} °F")
                st.success(f"{temp_value} °C = {kelvin:.1f} K")
                st.success(f"{temp_value} °C = {reamur:.1f} °Ré")

            elif temp_unit == "Fahrenheit":
                celsius = (temp_value - 32) * 5/9
                kelvin = celsius + 273.15
                reamur = celsius * 4/5
                st.success(f"{temp_value} °F = {celsius:.1f} °C")
                st.success(f"{temp_value} °F = {kelvin:.1f} K")
                st.success(f"{temp_value} °F = {reamur:.1f} °Ré")

            elif temp_unit == "Kelvin":
                celsius = temp_value - 273.15
                fahrenheit = (celsius * 9/5) + 32
                reamur = celsius * 4/5
                st.success(f"{temp_value} K = {celsius:.1f} °C")
                st.success(f"{temp_value} K = {fahrenheit:.1f} °F")
                st.success(f"{temp_value} K = {reamur:.1f} °Ré")

            elif temp_unit == "Reamur":
                celsius = temp_value * 5/4
                fahrenheit = (celsius * 9/5) + 32
                kelvin = celsius + 273.15
                st.success(f"{temp_value} °Ré = {celsius:.1f} °C")
                st.success(f"{temp_value} °Ré = {fahrenheit:.1f} °F")
                st.success(f"{temp_value} °Ré = {kelvin:.1f} K")

                
    elif conversion_type == "Tekanan":
        st.subheader("Konversi Tekanan")
        pressure_value = st.number_input("Masukkan nilai tekanan:")
        pressure_unit = st.selectbox("Pilih satuan tekanan:", ["Pascal", "hPa", "Bar", "Atmosfer", "Torr", "mmHg"])
    
        if st.button("Konversi"):
            if pressure_unit == "Pascal":
                hpa = pressure_value / 100
                bar = pressure_value / 1e5
                atm = pressure_value / 101325
                torr = pressure_value * 0.00750062
                mmhg = pressure_value / 133.322
                st.success(f"{pressure_value} Pa = {hpa:.2f} hPa")
                st.success(f"{pressure_value} Pa = {bar:.5f} Bar")
                st.success(f"{pressure_value} Pa = {atm:.5f} atm")
                st.success(f"{pressure_value} Pa = {torr:.5f} Torr")
                st.success(f"{pressure_value} Pa = {mmhg:.5f} mmHg")
    
            elif pressure_unit == "hPa":
                pascal = pressure_value * 100
                bar = pascal / 1e5
                atm = pascal / 101325
                torr = pascal * 0.00750062
                mmhg = pascal / 133.322
                st.success(f"{pressure_value} hPa = {pascal:.2f} Pa")
                st.success(f"{pressure_value} hPa = {bar:.4f} Bar")
                st.success(f"{pressure_value} hPa = {atm:.5f} atm")
                st.success(f"{pressure_value} hPa = {torr:.5f} Torr")
                st.success(f"{pressure_value} hPa = {mmhg:.5f} mmHg")
    
            elif pressure_unit == "Bar":
                pascal = pressure_value * 1e5
                hpa = pascal / 100
                atm = pressure_value / 1.01325
                torr = pressure_value * 750.062
                mmhg = pascal / 133.322
                st.success(f"{pressure_value} Bar = {pascal:.2f} Pa")
                st.success(f"{pressure_value} Bar = {hpa:.2f} hPa")
                st.success(f"{pressure_value} Bar = {atm:.5f} atm")
                st.success(f"{pressure_value} Bar = {torr:.5f} Torr")
                st.success(f"{pressure_value} Bar = {mmhg:.5f} mmHg")
    
            elif pressure_unit == "Atmosfer":
                pascal = pressure_value * 101325
                hpa = pascal / 100
                bar = pressure_value * 1.01325
                torr = pressure_value * 760
                mmhg = pascal / 133.322
                st.success(f"{pressure_value} atm = {pascal:.2f} Pa")
                st.success(f"{pressure_value} atm = {hpa:.2f} hPa")
                st.success(f"{pressure_value} atm = {bar:.5f} Bar")
                st.success(f"{pressure_value} atm = {torr:.2f} Torr")
                st.success(f"{pressure_value} atm = {mmhg:.2f} mmHg")
    
            elif pressure_unit == "Torr":
                pascal = pressure_value / 0.00750062
                hpa = pascal / 100
                bar = pressure_value / 750.062
                atm = pressure_value / 760
                mmhg = pascal / 133.322
                st.success(f"{pressure_value} Torr = {pascal:.2f} Pa")
                st.success(f"{pressure_value} Torr = {hpa:.2f} hPa")
                st.success(f"{pressure_value} Torr = {bar:.5f} Bar")
                st.success(f"{pressure_value} Torr = {atm:.5f} atm")
                st.success(f"{pressure_value} Torr = {mmhg:.5f} mmHg")
    
            elif pressure_unit == "mmHg":
                pascal = pressure_value * 133.322
                hpa = pascal / 100
                bar = pascal / 1e5
                atm = pascal / 101325
                torr = pascal * 0.00750062
                st.success(f"{pressure_value} mmHg = {pascal:.2f} Pa")
                st.success(f"{pressure_value} mmHg = {hpa:.2f} hPa")
                st.success(f"{pressure_value} mmHg = {bar:.5f} Bar")
                st.success(f"{pressure_value} mmHg = {atm:.5f} atm")
                st.success(f"{pressure_value} mmHg = {torr:.5f} Torr")

    elif conversion_type == "Volume":
        st.subheader("Konversi Volume")
        volume_value = st.number_input("Masukkan nilai volume:")
        volume_unit = st.selectbox("Pilih satuan volume:", ["Liter", "Mililiter", "dm³", "Cubic Meter"])

        if st.button("Konversi"):
            if volume_unit == "Liter":
                milliliter = volume_value * 1000
                cubic_meter = volume_value / 1000
                dm3 = volume_value  # 1 liter = 1 dm³
                st.success(f"{volume_value} L = {milliliter:.2f} mL")
                st.success(f"{volume_value} L = {cubic_meter:.5f} m³")
                st.success(f"{volume_value} L = {dm3:.5f} dm³")
            elif volume_unit == "Mililiter":
                liter = volume_value / 1000
                cubic_meter = liter / 1000
                dm3 = liter  # 1 liter = 1 dm³
                st.success(f"{volume_value} mL = {liter:.2f} L")
                st.success(f"{volume_value} mL = {cubic_meter:.5f} m³")
                st.success(f"{volume_value} mL = {dm3:.5f} dm³")
            elif volume_unit == "dm³":
                liter = volume_value  # 1 dm³ = 1 liter
                milliliter = liter * 1000
                cubic_meter = liter / 1000
                st.success(f"{volume_value} dm³ = {liter:.2f} L")
                st.success(f"{volume_value} dm³ = {milliliter:.2f} mL")
                st.success(f"{volume_value} dm³ = {cubic_meter:.5f} m³")
            elif volume_unit == "Cubic Meter":
                liter = volume_value * 1000
                milliliter = liter * 1000
                dm3 = liter  # 1 liter = 1 dm³
                st.success(f"{volume_value} m³ = {liter:.2f} L")
                st.success(f"{volume_value} m³ = {milliliter:.2f} mL")
                st.success(f"{volume_value} m³ = {dm3:.5f} dm³")

    elif conversion_type == "Massa":
        st.subheader("Konversi Massa")
        mass_value = st.number_input("Masukkan nilai massa:")
        mass_unit = st.selectbox("Pilih satuan massa:", ["Kilogram", "Gram", "Miligram"])

        if st.button("Konversi"):
            if mass_unit == "Kilogram":
                gram = mass_value * 1000
                milligram = mass_value * 1e6
                st.success(f"{mass_value} kg = {gram:.2f} g")
                st.success(f"{mass_value} kg = {milligram:.2f} mg")
            elif mass_unit == "Gram":
                kilogram = mass_value / 1000
                milligram = mass_value * 1000
                st.success(f"{mass_value} g = {kilogram:.5f} kg")
                st.success(f"{mass_value} g = {milligram:.2f} mg")
            elif mass_unit == "Miligram":
                gram = mass_value / 1000
                kilogram = gram / 1000
                st.success(f"{mass_value} mg = {gram:.5f} g")
                st.success(f"{mass_value} mg = {kilogram:.5f} kg")
                
    elif conversion_type == "Konsentrasi":
        st.subheader("🔁 Konversi Konsentrasi")
    
        conversion_value = st.number_input("Masukkan nilai konsentrasi:")
        conversion_unit = st.selectbox(
            "Pilih satuan konsentrasi:",
            ["Molaritas (M)", "Normalitas (N)", "Persen (% (b/v))", "Persen (% (b/b))", "ppm", "ppb", "ppt"]
        )
    
        valency = st.number_input("Masukkan valensi (jika diperlukan):", min_value=1, value=1)
        density = st.number_input("Masukkan bobot jenis/densitas (g/mL):", min_value=0.0, value=1.0)
        mol_weight = st.number_input("Masukkan bobot molekul (g/mol):", min_value=0.0, value=1.0)

        if st.button("Konversi"):
            if conversion_unit == "Molaritas (M)":
                normality = conversion_value * valency
            
                # Rumus benar untuk % b/v: (M * Mr) / 10
                percent_bv = (conversion_value * mol_weight) / 10
            
                # Rumus benar untuk % b/b: (M * Mr) / (ρ * 10)
                percent_bb = (conversion_value * mol_weight) / (density * 10) if density > 0 else 0
            
                st.success(f"{conversion_value:.4f} M = {normality:.2f} N")
                st.success(f"{conversion_value:.4f} M = {percent_bv:.2f} % (b/v)")
                st.success(f"{conversion_value:.4f} M = {percent_bb:.2f} % (b/b)")
    
            elif conversion_unit == "Normalitas (N)":
                molarity = conversion_value / valency
                percent_bv = (molarity * mol_weight) / 10
                percent_bb = (molarity * mol_weight) / (density * 10) if density > 0 else 0
                st.success(f"{conversion_value:.4f} N = {molarity:.4f} M")
                st.success(f"{conversion_value:.4f} N = {percent_bv:.2f} % (b/v)")
                st.success(f"{conversion_value:.4f} N = {percent_bb:.2f} % (b/b)")
                
            elif conversion_unit == "Persen (% (b/v))":
                molarity = (conversion_value * 10) / mol_weight if mol_weight > 0 else 0
                normality = molarity * valency
                percent_bb = conversion_value / density if density > 0 else 0
                st.success(f"{conversion_value:.4f} % (b/v) = {molarity:.4f} M")
                st.success(f"{conversion_value:.4f} % (b/v) = {normality:.4f} N")
                st.success(f"{conversion_value:.4f} % (b/v) = {percent_bb:.2f} % (b/b)")
    
            elif conversion_unit == "Persen (% (b/b))":
                molarity = (conversion_value * density * 10) / mol_weight if mol_weight > 0 and density > 0 else 0
                normality = molarity * valency
                percent_bv = conversion_value * density  # % (b/v) = % (b/b) × ρ
                st.success(f"{conversion_value:.4f} % (b/b) = {molarity:.4f} M")
                st.success(f"{conversion_value:.4f} % (b/b) = {normality:.4f} N")
                st.success(f"{conversion_value:.4f} % (b/b) = {percent_bv:.2f} % (b/v)")
    
            elif conversion_unit == "ppm":
                ppb = conversion_value * 1000
                ppt = ppb * 1000
                st.success(f"{conversion_value:.2f} ppm = {ppb:.2f} ppb")
                st.success(f"{conversion_value:.2f} ppm = {ppt:.2f} ppt")
    
            elif conversion_unit == "ppb":
                ppm = conversion_value / 1000
                ppt = conversion_value * 1000
                st.success(f"{conversion_value:.2f} ppb = {ppm:.2f} ppm")
                st.success(f"{conversion_value:.2f} ppb = {ppt:.2f} ppt")
    
            elif conversion_unit == "ppt":
                ppm = conversion_value / 1_000_000
                ppb = conversion_value / 1000
                st.success(f"{conversion_value:.2f} ppt = {ppm:.6f} ppm")
                st.success(f"{conversion_value:.2f} ppt = {ppb:.2f} ppb")

# ==================== STANDARDISASI =====================
elif menu == "Standardisasi":
    st.header("🧪 Standardisasi Larutan")
    st.write("Dalam Normalitas")

    ulangan = st.radio("Pilih jumlah ulangan", ["Duplo (2)", "Triplo (3)"])
    n = 2 if "Duplo" in ulangan else 3

    # Variabel input
    mg_Standar_Baku_Primer = []
    mL_Titran = []
    BE_Standar_Baku_Primer = []
    f_pengali = []
    normalitas = []

    # Buat kolom
    kolom = st.columns(n)

    for i in range(n):
        with kolom[i]:
            st.markdown(f"### Ulangan {i+1}")
            mg = st.number_input(f"Standar baku primer (mg)", key=f"mg_{i}")
            mL = st.number_input(f"Titran (mL)", key=f"ml_{i}")
            BE = st.number_input(f"Bobot Ekuivalen (mg/mgrek)", key=f"be_{i}")
            f = st.number_input(f"Faktor pengali", key=f"f_{i}", value=1.0)

            mg_Standar_Baku_Primer.append(mg)
            mL_Titran.append(mL)
            BE_Standar_Baku_Primer.append(BE)
            f_pengali.append(f)

    # Tombol hitung
    if st.button("🔍 Hitung Normalitas"):
        for i in range(n):
            try:
                N = mg_Standar_Baku_Primer[i] / (mL_Titran[i] * BE_Standar_Baku_Primer[i] * f_pengali[i])
            except ZeroDivisionError:
                N = 0
            normalitas.append(N)

        # Tampilkan tabel normalitas
        df_dict = {f"Ulangan {i+1}": [normalitas[i]] for i in range(n)}
        df = pd.DataFrame(df_dict, index=["Normalitas (N)"])
        st.dataframe(df)

        mean_N = np.mean(normalitas)
        st.markdown("### Statistik")
        st.write(f"**Rata-rata Normalitas**: {mean_N:.4f} N")

        if n == 2:
            # %RPD untuk duplo
            rpd = abs(normalitas[0] - normalitas[1]) / ((normalitas[0] + normalitas[1]) / 2) * 100
            st.write(f"**%RPD (Relative Percent Difference)**: {rpd:.2f}%")
        else:
            # %RSD untuk triplo atau lebih
            std_N = np.std(normalitas, ddof=1)
            rsd = (std_N / mean_N) * 100 if mean_N else 0
            st.write(f"**Standar Deviasi (SD)**: {std_N:.4f}")
            st.write(f"**%RSD (Relative Standard Deviation)**: {rsd:.2f}%")
