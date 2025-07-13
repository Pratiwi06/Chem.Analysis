import streamlit as st

st.title("Chemical Analysis")
st.title("_chemical_ is :blue[cool] :sunglasses:")
import streamlit as st
import slide1
import slide2
import slide3  # Kalau kamu tambah slide lain

st.set_page_config(page_title="Slide Interaktif", layout="wide")

st.title("📊 Aplikasi Slide Interaktif Berbasis Streamlit")

# Tabs untuk setiap slide
tab1, tab2, tab3 = st.tabs(["🧪 Slide 1", "📈 Slide 2", "📘 Slide 3"])

with tab1:
    slide1.show()

with tab2:
    slide2.show()

with tab3:
    slide3.show()
