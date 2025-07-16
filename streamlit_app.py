# ==================== TAB 6 =====================
with tab6:
    st.header("\U0001F9EA Perhitungan Titrasi Kimia")
    st.markdown("Masukkan data titrasi duplo untuk menghitung **Normalitas Sampel, Rata-rata, SD**, dan **%RSD**. Serta input bobot ekuivalen dan bobot baku primer untuk standardisasi.")

    jenis_titrasi = st.selectbox("Pilih Jenis Titrasi", [
        "Asam-Basa", "Argentometri", "Kompleksiometri", "Permanganometri"
    ])

    st.subheader("Input Data Titrasi")
    col1, col2 = st.columns(2)
    with col1:
        V1 = st.number_input("Volume Titrasi ke-1 (mL)", min_value=0.0, step=0.01, format="%.2f")
        N_titran = st.number_input("Normalitas Titran (standar)", min_value=0.0, step=0.0001, format="%.4f")
        bobot_baku = st.number_input("Bobot Baku Primer (g)", min_value=0.0, step=0.0001, format="%.4f")
    with col2:
        V2 = st.number_input("Volume Titrasi ke-2 (mL)", min_value=0.0, step=0.01, format="%.2f")
        V_sampel = st.number_input("Volume Sampel (mL)", min_value=0.0, step=0.01, format="%.2f")
        bobot_ekivalen = st.number_input("Bobot Ekuivalen (g/eq)", min_value=0.0001, step=0.0001, format="%.4f")

    if V1 > 0 and V2 > 0 and V_sampel > 0 and bobot_ekivalen > 0 and bobot_baku > 0:
        volumes = np.array([V1, V2])
        avg_V = np.mean(volumes)
        std_V = np.std(volumes, ddof=1)
        rsd = (std_V / avg_V) * 100 if avg_V != 0 else 0

        N_sampel = (N_titran * avg_V) / V_sampel if V_sampel != 0 else 0
        N_standar = (bobot_baku / bobot_ekivalen) / (avg_V / 1000) if avg_V > 0 else 0

        st.subheader("\U0001F4CA Hasil Perhitungan Titrasi")
        st.write(f"**Jenis Titrasi:** {jenis_titrasi}")
        st.write(f"**Rata-rata Volume Titrasi:** {avg_V:.2f} mL")
        st.write(f"**Standar Deviasi (SD):** {std_V:.4f}")
        st.write(f"**%RSD:** {rsd:.2f}%")
        st.success(f"**Normalitas Sampel:** {N_sampel:.4f} N")
        st.success(f"**Normalitas dari Standardisasi:** {N_standar:.4f} N")
    else:
        st.subheader("\U0001F4CA Hasil Perhitungan Titrasi")
        st.info("Silakan isi seluruh input (termasuk bobot ekuivalen dan bobot baku primer) untuk melihat hasil perhitungan.")
