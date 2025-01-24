from PIL import Image
import os

def compress_images(input_folder, output_folder, quality=50):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            output_path = os.path.join(output_folder, filename)
            
            # Convert PNG to JPEG to reduce file size
            if filename.endswith(".png"):
                output_path = output_path.replace(".png", ".jpg")
                img = img.convert("RGB")
            
            img.save(output_path, optimize=True, quality=quality)
            print(f"Compressed {filename} and saved to {output_path}")

input_folder = 'image2'
output_folder = 'compressed_image2'
compress_images(input_folder, output_folder, quality=30)