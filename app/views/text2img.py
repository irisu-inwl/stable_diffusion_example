import streamlit as st

from model.stable_diffusion import generate_image

def view():
    st.title('Text to Image')
    prompt = st.text_input('prompt', '')
    button_state = st.button('generate')
    if button_state is True:
        images = generate_image(prompts = [prompt])
        st.image(
            images[0], caption='generated images',
            use_column_width=True
        )

