
# Pillow is a powerful and easy-to-use Python Imaging Library (PIL) fork that allows you to:
# Open, display, and save images in various formats
# Perform image processing (rotate, crop, resize, filter, etc.)
# Draw shapes and text
# Work with color modes, transparency, and pixel data
# Enhance or analyze images

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageOps

# Open and Basic Info 
# i = Image.open(r"C:\Users\Diksha Kolhe\OneDrive\Desktop\Python Advance\Regular expresion\diksha.JPG")
# # i.show()
# print("filename:",i.filename)
# print("Format:", i.format)
# print("Size:", i.size)
# print("Mode:", i.mode)

# #Saving in Different Formats 
# i.save("output.png")  # Save as PNG


# # Image Rotation 
# # Rotate the image by 45 degrees
# # expand=True resizes the image to fit the entire rotated image
# # fillcolor="red" fills the background corners created by rotation
# rotated = i.rotate(45, expand=True, fillcolor='green')
# # rotated.show()

# #  Resize 
# resized = i.resize((300, 300))
# # resized.show()

# #  Crop 
# # Crop the image to a box from (50, 50) to (200, 200)
# crop = i.crop((50, 50, 200, 200))
# # crop.show()

# # Convert Color Modes 
# # Convert the image to grayscale (L mode)
# gray = i.convert("L")
# # gray.show()

# # Convert the image to RGBA mode (adds alpha channel)
# rgba = i.convert("RGBA")
# # rgba.show()

# #  Image Filter Effects 
# blurred = i.filter(ImageFilter.BLUR)
# # blurred.show()
# # 
# sharpened = i.filter(ImageFilter.SHARPEN)
# # sharpened.show()

# edges = i.filter(ImageFilter.FIND_EDGES)
# # edges.show()

# # Image Enhancements 
# # Brightness
# enhancer = ImageEnhance.Brightness(i)
# bright_img = enhancer.enhance(1.2)  # 1.0 = original, >1 = brighter
# # bright_img.show()

# # Contrast
# contrast = ImageEnhance.Contrast(i).enhance(1.8)
# # contrast.show()

# # Sharpness
# sharp = ImageEnhance.Sharpness(i).enhance(3.0)
# # sharp.show()

# # Color
# color = ImageEnhance.Color(i).enhance(2.0)
# # color.show()

# #Drawing on Image 
# draw = ImageDraw.Draw(i)

# # Rectangle
# draw.rectangle([50, 50, 200, 200], fill="blue", outline="white", width=3)
# # i.show()

# # Ellipse
# draw.ellipse([220, 50, 350, 200], fill="yellow", outline="black")
# # i.show()

# # Line
# draw.line((400, 60, 600, 60), fill="red", width=4)
# # i.show()


# # Text
# font = ImageFont.load_default()
# font=ImageFont.truetype("arial.ttf",30)
# draw.text((400, 200), "Hello PIL!", fill="red", font=font)
# # i.show()

# # #  Flip and Mirror 
# flipped = ImageOps.flip(i)  # Vertical flip
# # flipped.show()

# mirrored = ImageOps.mirror(i)  # Horizontal flip
# # mirrored.show()


# # # Paste One Image onto Another 
# # Create new blank canvas
# canvas = Image.new("RGBA", (800, 600), "Red")


# # # Paste original image onto canvas
# canvas.paste(i, (100, 100))  # Paste at x=100, y=100
#canvas.show()


##Transperency 
# i = Image.open(r"C:\Users\Diksha Kolhe\OneDrive\Desktop\Python Advance\Regular expresion\diksha.JPG")
#new=Image.open(r"C:\Users\Diksha Kolhe\OneDrive\Desktop\Python Advance\Regular expresion\butterfly.JPG")
# rgba1=i.convert("RGBA")
# rgba2=new.convert("RGBA")
# resized1= rgba1.resize((rgba2.width,rgba2.height))
# a=Image.alpha_composite(rgba1,rgba2)
# a.show()

##Watermark add
a=Image.open(r"C:\Users\Diksha Kolhe\OneDrive\Desktop\Python Advance\Regular expresion\butterfly.JPG").convert("RGBA")
o=Image.new("RGBA", a.size,(255,255,255,0))
draw=ImageDraw.Draw(o)
font=ImageFont.truetype("arial.ttf",40)
draw.text((a.width-180,a.height-100), "Hello PIL!", fill="pink", font=font)
s=Image.alpha_composite(a,o)
s.show()
