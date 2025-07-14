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
    elements = {
        "hidrogen": {"nomor_atom": 1, "massa_atom": 1.008},
        "helium": {"nomor_atom": 2, "massa_atom": 4.0026},
        "litium": {"nomor_atom": 3, "massa_atom": 6.94},
        "berilium": {"nomor_atom": 4, "massa_atom": 9.0122},
        "boron": {"nomor_atom": 5, "massa_atom": 10.81},
        "karbon": {"nomor_atom": 6, "massa_atom": 12.01},
        "nitrogen": {"nomor_atom": 7, "massa_atom": 14.01},
        "oksigen": {"nomor_atom": 8, "massa_atom": 16.00},
        "fluorin": {"nomor_atom": 9, "massa_atom": 19.00},
        "neon": {"nomor_atom": 10, "massa_atom": 20.18},
    }
    user_input = st.text_input("Masukkan nama unsur (contoh: karbon)").lower()
    if user_input in elements:
        st.success(f"Nomor Atom: {elements[user_input]['nomor_atom']}, Massa Atom: {elements[user_input]['massa_atom']}")
    elif user_input:
        st.warning("Unsur tidak ditemukan dalam database.")

# ==================== TAB 3 =====================
with tab3:
    st.header(":bar_chart: Regresi Linear")

    x_input = st.text_input("Konsentrasi Standar (x), pisahkan koma", "")
    y_input = st.text_input("Absorbansi Standar (y), pisahkan koma", "")
    y_sample = st.text_input("Absorbansi Rata-Rata Sampel (Y₀) [Opsional]", "")

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
                sum_sq_x = np.sum((x_vals - x_mean) ** 2)
                r = np.corrcoef(x_vals, y_vals)[0, 1]
                R2 = r ** 2

                st.success(f"Persamaan regresi: y = {m:.4f}x + {b:.4f}")
                st.write(f"• Slope (m): {m:.4f}")
                st.write(f"• Intercept (b): {b:.4f}")
                st.write(f"Koefisien Korelasi (r): {r:.4f}")
                st.write(f"Koefisien Determinasi (R²): {R2:.4f}")

                RSD = Sy / y_mean * 100 if y_mean else 0.0
                st.write(f"RSD kurva regresi: {RSD:.2f}%")

                if y_sample:
                    try:
                        y_sample_val = float(y_sample)
                        mu_reg = (Sy / abs(m)) * np.sqrt(1 + (1 / n) + ((y_sample_val - y_mean) ** 2) / (m**2 * sum_sq_x)) if m else 0.0
                        st.info(f"Ketidakpastian regresi (μ_reg): {mu_reg:.4f}")
                    except:
    st.warning("Masukkan nilai numerik untuk absorbansi sampel.")
else:
    st.info("μ_reg tidak dihitung karena absorbansi sampel (Y₀) tidak diisi.")
                        st.warning("Masukkan nilai numerik untuk absorbansi sampel.")

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
