            ax.scatter(x_vals, y_vals, label="Data Kalibrasi", color="blue")
            ax.plot(x_vals, y_fit, label=f"Regresi: y = {m:.2f}x + {b:.2f}", color="red")
            ax.axhline(y_sampel, color='green', linestyle='--', label=f"Abs Sampel = {y_sampel}")
            ax.axvline(x_sampel, color='orange', linestyle=':', label=f"x Sampel = {x_sampel:.2f}")
            ax.set_xlabel("Konsentrasi (x)")
            ax.set_ylabel("Absorbansi (y)")
            ax.set_title("Kurva Kalibrasi dan Absorbansi Sampel")
            ax.legend()
            st.pyplot(fig)
            # Hitung ketidakpastian diperluas
            if st.button("🎯 Hitung Ketidakpastian"):
                uc = mu_reg
                U = 2 * uc
                st.header("📤 Hasil Akhir")
                st.write(f"Ketidakpastian gabungan (uc): **{uc:.4f}**")
                st.write(f"Ketidakpastian diperluas (U, k=2): **{U:.4f}**")
                st.success(f"🔬 Konsentrasi Sampel: **{x_sampel:.2f} ± {U:.2f}** (95% CI)")
    except Exception as e:
        st.warning(f"Masukkan data numerik yang valid. Kesalahan: {e}")
# ==================== TAB 4 s.d. 6 =====================
with tab4:
    st.header("Ketidakpastian Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
with tab5:
    st.header("Konversi Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
with tab6:
    st.header("Titrasi Placeholder")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
