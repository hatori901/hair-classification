import streamlit as st


def show_home():
    st.image("images/illustration.webp", use_column_width=True)
    st.write("""
    Selamat datang di aplikasi klasifikasi rambut! 
    Aplikasi ini dirancang untuk membantu Anda mengetahui jenis rambut Anda berdasarkan foto yang Anda unggah.
    Cukup unggah foto rambut Anda, dan kami akan memberikan klasifikasi yang sesuai.
    """)