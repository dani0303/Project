from PIL import Image
import matplotlib.pyplot as plt

image = input("Enter the path to the image: ")

readable_image = Image.open(image)
pixelate_image = readable_image.resize((32, 32), Image.BILINEAR)

new_size = (1000, 1000)
new_image = pixelate_image.resize(new_size, Image.NEAREST)
plt.imshow(new_image)
plt.show()
