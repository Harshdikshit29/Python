# streamlit run app1/hello.py        (run file in command prompt)

import streamlit as st
from PIL import Image

st.title("Sample App")
st.header("this is header")
st.subheader("this is subheader")

image = st.camera_input("camera input", key="camera_input")
if image:
    im = Image.open(image)
    # purple gradient image
    color = st.color_picker("Pick a color", "#00f900")
    im2 = Image.new("RGB", im.size, color)
    # overlay two images
    im = Image.blend(im,im2, 0.5)
    # resize by 30%
    im = im.resize((int(im.size[0]*0.3), int(im.size[1]*0.3)))
    
    st.sidebar.image(im)
    
    filename = st.text_input("Save as", "image.png")
    if st.button("Save"):
        im.save(filename)
        st.snow()