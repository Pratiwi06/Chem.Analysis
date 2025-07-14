# ==================== PAGE CONFIG & TITLE =====================
st.set_page_config(page_title="Chemical Analysis App", layout="wide")
st.title("Chemical Analysis")
st.title("_chemical_ is :blue[cool] :sunglasses:")

# ==================== TAB 1 =====================
with tab1:
    st.header("📏 Regresi Linear dan Ketidakpastian Pengukuran")
    st.subheader("Selamat datang di aplikasi analisis kimia!")
    st.write("Gunakan tab-tab di atas untuk menjelajahi fitur seperti regresi, konversi satuan, dan tabel periodik interaktif.")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

# ==================== TAB 2 =====================
with tab2:
    st.header("Tabel Periodik")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

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

        # Tombol Hitung
    hitung = st.button("🔍 Hitung")

    # Perform calculation when hitung pressed
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
            mu_reg = (Sy / m) * np.sqrt((1 / n) + ((np.mean(x_vals) - x_mean) ** 2 / sum_sq_x)) if m else 0.0
            r = np.corrcoef(x_vals, y_vals)[0, 1]
            R2 = r ** 2

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
