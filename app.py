import streamlit as st
from PIL import Image, ImageOps, ImageColor
import numpy as np
from rembg import remove

st.title("Pixie-Palette:Transform Your Image Backgrounds with Colorful Magic")

# Upload an image in png, jpeg, or jpg format
uploaded_file = st.file_uploader("Upload an image (png, jpeg, jpg)", type=["png", "jpeg", "jpg"])

# Color picker for background color
background_color = st.color_picker("Pick a new background color", "#FFFFFF")

if uploaded_file is not None:
    # Open the uploaded image and remove the background
    image = Image.open(uploaded_file)
    image_no_bg = remove(image)  # Remove the background using `rembg`

    # Convert image to RGBA to manipulate transparency
    image_no_bg = image_no_bg.convert("RGBA")
    data = np.array(image_no_bg)
    
    # Replace transparent areas with the chosen color
    new_color = ImageColor.getrgb(background_color)
    mask = data[..., 3] == 0  # Detect transparent pixels
    data[..., :3][mask] = new_color  # Replace with new color
    data[..., 3][mask] = 255  # Ensure the new background is opaque

    # Convert the numpy array back to an image
    modified_image = Image.fromarray(data, "RGBA")
    
    # Display the original and modified images side by side
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(image, caption="Original Image", use_container_width=True)
    
    with col2:
        st.image(modified_image, caption="Modified Image", use_container_width=True)

    # Option to download the modified image
    st.download_button(
        label="Download Modified Image",
        data=modified_image.tobytes("raw", "RGBA"),
        file_name="modified_image.png",
        mime="image/png"
    )
