# Pixie-Palette-Transform-Your-Image-Backgrounds-with-Colorful-Magic

<img width="543" alt="Image20241116172619" src="https://github.com/user-attachments/assets/01435d9a-45eb-4461-adf9-d158675c2ea7">



## Overview
This Streamlit app allows users to upload images and change their background color easily. Whether you're looking to remove the background or replace it with a new color of your choice, this app handles it seamlessly using advanced libraries like `rembg` and `Pillow`.

## Features
- **User-Friendly Image Upload**: Upload `.png`, `.jpeg`, or `.jpg` files.
- **Automatic Background Removal**: Leveraging the `rembg` library for precise background detection.
- **Customizable Background Color**: Choose any color to replace the background with a simple color picker.
- **Side-by-Side Comparison**: View the original and modified images side by side for easy comparison.
- **Download Functionality**: Download your modified image with a single click.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/image-background-color-changer.git
    cd image-background-color-changer
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run the App
Run the following command in your terminal:
```bash
streamlit run app.py
```


## How to Use
Upload an image in .png, .jpeg, or .jpg format.
Choose your preferred background color using the color picker.
View the original and modified images side by side.
Download the modified image by clicking the "Download Modified Image" button.

## Technologies Used
- **Streamlit**: For building the web app interface.
- **Pillow (PIL)**: For image processing and manipulation.
- **rembg**: For efficient and accurate background removal.
- **NumPy**: For array manipulation.

## Files in the Repository
- **app.py**: The main script for running the Streamlit app.
- **requirements.txt** : Contains a list of all the dependencies needed for the app.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

