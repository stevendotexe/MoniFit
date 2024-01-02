import sys
import os
import base64

def get_embedded_image():
    # Get the path to the directory containing the script or executable
    base_path = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.abspath(".")

    # Specify the relative path to the embedded image (e.g., logo.png)
    image_path = os.path.join(base_path, 'logo.png')

    # Read the embedded image as bytes
    with open(image_path, 'rb') as file:
        image_data = file.read()

    return image_data

def main():
    pass
if __name__ == '__main__': 
    main()
