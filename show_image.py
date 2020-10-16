from PIL import Image

jpeggy = Image.open("img-1.png")

jpeggy.show()

jpeggy = jpeggy.rotate(45)
jpeggy.show()