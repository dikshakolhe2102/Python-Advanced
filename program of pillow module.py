from PIL import Image,ImageFont,ImageDraw
import random,string
##
# i=input("Enter text:")
# canvas = Image.new("RGBA", (800, 600), "gray")
# canvas.show()
# draw=ImageDraw.Draw(canvas)
# font = ImageFont.load_default()
# draw.text((100,200),i,fill="black",font=font)
# canvas.show()

# canvas=Image.new("RGBA", (800, 600), "gray")
# canvas.show()
# a=""
# b=string.ascii_letters+string.digits
# for i in range(6):
#     a=a+random.choice(b)
# font = ImageFont.load_default()
# draw=ImageDraw.Draw(canvas)
# draw.text((100,200),a,fill="white",font=font)
# canvas.show()



canvas=Image.new("RGBA", (400, 800), "gray")
canvas.show()
h,w=canvas.size
print(h,w)
a=""
b=string.ascii_letters+string.digits
for i in range(6):
    a=a+random.choice(b)
font = ImageFont.truetype("arial.ttf",30)
draw=ImageDraw.Draw(canvas)
draw.text((h-100,w-100),a,fill="white",font=font)
canvas.show()


