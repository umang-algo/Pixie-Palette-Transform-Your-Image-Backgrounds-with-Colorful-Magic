import streamlit as st
from PIL import Image, ImageOps, ImageColor, ImageFilter
import numpy as np
from rembg import remove
from io import BytesIO

st.title("Pixie-Palette: Transform Your Image Backgrounds with Colorful Magic")

# Upload an image in png, jpeg, or jpg format
uploaded_file = st.file_uploader("Upload an image (png, jpeg, jpg)", type=["png", "jpeg", "jpg"])

# Choose background option: color or image
bg_option = st.radio("Choose background type", ("Solid Color", "Image"))

# Color picker for background color
background_color = None
background_image = None
modified_image = None  # Initialize the variable

if bg_option == "Solid Color":
    background_color = st.color_picker("Pick a new background color", "#FFFFFF")
elif bg_option == "Image":
    background_image = st.file_uploader("Upload a background image (png, jpeg, jpg)", type=["png", "jpeg", "jpg"])

if uploaded_file is not None:
    # Open the uploaded image and remove the background
    image = Image.open(uploaded_file)
    image_no_bg = remove(image)  # Remove the background using `rembg`

    # Convert image to RGBA to manipulate transparency
    image_no_bg = image_no_bg.convert("RGBA")
    data = np.array(image_no_bg)

    # Create a mask for transparent areas
    mask = data[..., 3] == 0  # Detect transparent pixels

    if bg_option == "Solid Color":
        # Replace transparent areas with the chosen color
        new_color = ImageColor.getrgb(background_color)
        data[..., :3][mask] = new_color  # Replace with new color
        data[..., 3][mask] = 255  # Ensure the new background is opaque

        # Convert the numpy array back to an image
        modified_image = Image.fromarray(data, "RGBA")
    elif bg_option == "Image" and background_image is not None:
        # Open the background image and resize to match the original image dimensions
        bg_image = Image.open(background_image).convert("RGBA")
        bg_image = bg_image.resize(image_no_bg.size)

        # Combine the foreground and background images
        modified_image = Image.alpha_composite(bg_image, image_no_bg)

    # Apply a slight blur to refine edges if a modified image is created
    if modified_image is not None:
        modified_image = modified_image.filter(ImageFilter.SMOOTH)

    # Display the original and modified images side by side
    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption="Original Image", use_container_width=True)

    if modified_image is not None:
        with col2:
            st.image(modified_image, caption="Modified Image", use_container_width=True)

        # Convert the modified image to a byte stream in JPEG format
        buffer = BytesIO()
        modified_image.convert("RGB").save(buffer, format="JPEG", quality=95)
        buffer.seek(0)

        # Option to download the modified image as JPEG
        st.download_button(
            label="Download Modified Image",
            data=buffer,
            file_name="modified_image.jpg",
            mime="image/jpeg"
        )
    else:
        st.warning("Please upload a background image for the 'Image' option.")
