import streamlit as st
from transformers import pipeline
from PIL import Image
import numpy as np

def show_detection():
    st.write("## Hair Detection")
    st.write("""
    1. Unggah foto rambut Anda.
    2. Klik tombol 'Deteksi Rambut'.
    """)

    # Load model
    classifier = pipeline("image-classification", model="erwinalam/image-classification")
    
    # Upload gambar
    uploaded_file = st.file_uploader("Pilih gambar model", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Menampilkan gambar yang diunggah
        image = Image.open(uploaded_file)
        st.image(image, caption='Gambar yang diunggah', use_column_width=True)

        # Klasifikasi gambar
        st.write("Menganalisis gambar...")
        predictions = classifier(image)

        st.html(
                f"""
                <div style="background-color:#f9f9f9; padding:10px; border-radius:10px; color: #000;">
                    <p><b>Hasil Klasifikasi:</b></p>
                    <p><b>Label:</b> {predictions[0]['label']}</p>
                    <p><b>Skor:</b> {predictions[0]['score']}</p>
                </div>
                """
            )

        