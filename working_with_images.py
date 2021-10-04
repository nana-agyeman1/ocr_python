from PIL import Image

im_file = "data/page_01.jpg"
im = Image.open(im_file)
# im.rotate(180).show()
im.save("temp/page_01.jpg")