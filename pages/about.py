import streamlit as st

def show_about():
    st.write("""
    ## Tentang Aplikasi
    Aplikasi ini dibuat untuk membantu Anda mengetahui jenis rambut Anda berdasarkan foto yang Anda unggah.
    Cukup unggah foto rambut Anda, dan kami akan memberikan klasifikasi yang sesuai.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.write("""
        #### Teknologi yang Digunakan
        - Streamlit
        - Hugging Face Transformers
        - PIL
        - Pytorch
        """)