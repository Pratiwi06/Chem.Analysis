import streamlit as st

st.title("Chemical Analysis")
st.title("_chemical_ is :blue[cool] :sunglasses:")
import streamlit as st

tab1, tab2, tab3, tab4, tab5, tab6= st.tabs(["Beranda", "Tabel Periodik", "Regresi", "Ketidakpastian", "Konversi", "Titrasi"])

with tab1:
    st.header("Regresi Linear ")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200) 
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
with tab4:
    st.header("Titrasi")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
with tab5:
    st.header("Titrasi")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
with tab6:
    st.header("Titrasi")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
