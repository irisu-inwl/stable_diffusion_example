
import streamlit as st
from views import img2img, text2img

selectbox_result = st.sidebar.selectbox(
    'Stable Diffusion',
    ('text2image', 'image2image')
)

if selectbox_result == 'text2image':
    text2img.view()
elif selectbox_result == 'image2image':
    img2img.view()