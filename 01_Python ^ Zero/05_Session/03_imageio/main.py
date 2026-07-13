import os
import imageio as img

images = os.listdir("images")
files = []

for image_name in images:
    path = os.path.join('images', image_name)
    file = img.imread(path)
    files.append(file)

img.mimsave("Animation.gif", files, duration=0.5, loop=0)
