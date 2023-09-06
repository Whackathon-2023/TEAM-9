from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import random
import sys
import os

def drastically_change_image(input_path, output_directory, iteration):
    img = Image.open(input_path)

    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Randomly select a drastic transformation
    choice = random.randint(1, 4)

    if choice == 1:
        # Apply a strong blur
        img = img.filter(ImageFilter.GaussianBlur(radius=5))
    elif choice == 2:
        # Invert colors
        img = ImageOps.invert(img)
    elif choice == 3:
        # Change color balance aggressively
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(random.choice([0.2, 2.0]))
    else:
        # Convert to grayscale and apply a strong contrast
        img = ImageOps.grayscale(img)
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2.0)

    # Construct an output path and save the modified image
    filename = os.path.basename(input_path)
    name, ext = os.path.splitext(filename)
    output_path = os.path.join(output_directory, f"{name}_variant_{iteration}{ext}")
    img.save(output_path)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python app.py [input_image_path] [output_directory] [number_of_versions]")
    else:
        input_path = sys.argv[1]
        output_directory = sys.argv[2]
        number_of_versions = int(sys.argv[3])
        for i in range(number_of_versions):
            drastically_change_image(input_path, output_directory, i)
