from PIL import Image
import streamlit as st

from model.stable_diffusion import generate_image

def view():
    st.title('Text to Image')
    prompt = st.text_input('prompt', '')
    uploaded_image = None
    uploaded_file = st.file_uploader('Choose a image file')
    if uploaded_file is not None:
        uploaded_image = Image.open(uploaded_file)
        st.image(
            uploaded_image, caption='upload images',
            use_column_width=True
        )
    button_state = st.button('generate')
    if button_state is True:
        images = generate_image([prompt], uploaded_image)
        st.image(
            images[0], caption='generated images',
            use_column_width=True
        )