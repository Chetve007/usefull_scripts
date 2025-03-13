from PIL import Image

Image.open("input.jpg").resize((500, 500)).save("output.jpg")
