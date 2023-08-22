from PIL import Image 
import os

image_folder = "images/"

if __name__ == "__main__":
    for filename in os.listdir(image_folder):
        name,extension = os.path.splitext(image_folder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(image_folder + filename)
            picture.save(image_folder + "compressed_" + filename, optimize = True, quality = 60)
        ##  os.remove(image_folder + filename)
            print(name + ":" + extension)
