mu_reg = (Sy / abs(m)) * np.sqrt((1 / n) + (np.mean((x_vals - x_mean) ** 2) / sum_sq_x)) if m else 0.0
                r = np.corrcoef(x_vals, y_vals)[0, 1]
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
