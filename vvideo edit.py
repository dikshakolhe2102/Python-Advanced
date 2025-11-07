from moviepy.editor import *
#c=VideoFileClip(r"C:\Users\Diksha Kolhe\OneDrive\Desktop\Python Advance\Regular expresion\vdo2.mp4")
#c.preview()
#sc=c.subclip(0,5)
#sc.preview()
# sc.write_videofile("out.mp4")
# a=c.write_gif("barish.gif")
# a.preview()
#rotated=c.rotate(180)
#rotated.preview()

# from PIL import Image
# if not hasattr(Image, 'ANTIALIAS'):
#     Image.ANTIALIAS = Image.Resampling.LANCZOS
# resized=c.resize(width=200)
# resized.preview()

#cut=c.cutout(0,5)
#cut.preview()

#mar=c.margin(20,color=(255,0,0))
#mar.preview()

# fast=c.fx(vfx.speedx,0.5)
#fast.preview()

# fast=c.fx(vfx.fadein,4)
# fast.preview()

# c3=VideoFileClip(r"C:\Users\Diksha Kolhe\OneDrive\Desktop\Python Advance\Regular expresion\vdo4.mp4")
# # slow=c3.fx(vfx.fadeout,4).fx(vfx.fadein,4)
# # slow.preview()

# v=c3.fx(vfx.blackwhite)
# # v.preview()

# f=c3.fx(vfx.loop,n=2)
#f.preview()
# a=f.write_videofile("di.mp4")

# c1=VideoFileClip(r"C:\Users\Diksha Kolhe\OneDrive\Desktop\Python Advance\Regular expresion\vdo1.mp4").subclip(0,6)
# c2=VideoFileClip(r"C:\Users\Diksha Kolhe\OneDrive\Desktop\Python Advance\Regular expresion\vdo3.mp4").subclip(0,6)
# v=concatenate_videoclips([c1,c2])
# v.write_videofile("Kolhe.mp4")

# au=c.without_audio()
# au.preview()

# duration=c.set_duration(8)
# duration.preview()

# c1=VideoFileClip(r"C:\Users\Diksha Kolhe\OneDrive\Desktop\Python Advance\Regular expresion\vdo1.mp4").subclip(0,6)
# c2=VideoFileClip(r"C:\Users\Diksha Kolhe\OneDrive\Desktop\Python Advance\Regular expresion\vdo2.mp4").subclip(0,6)
# c3=VideoFileClip(r"C:\Users\Diksha Kolhe\OneDrive\Desktop\Python Advance\Regular expresion\vdo3.mp4").subclip(0,6)
# c4=VideoFileClip(r"C:\Users\Diksha Kolhe\OneDrive\Desktop\Python Advance\Regular expresion\vdo4.mp4").subclip(0,6)

# layout=clips_array([[c1,c2],[c3,c4]])
# #layout.preview()
# arr=layout.write_videofile("diksha.mp4")

from moviepy.config import change_settings
change_settings({
    "IMAGEMAGICK_BINARY":"C:\\Program Files\\ImageMagick-7.1.2-Q16-HDRI\\magick.exe"
})
c1=VideoFileClip(r"C:\Users\Diksha Kolhe\OneDrive\Desktop\Python Advance\Regular expresion\vdo2.mp4")
# txt=TextClip("Hello",fontsize=50,color="Red")
# txt=txt.set_position((200,300)).set_duration(5)
# v=CompositeVideoClip([c1,txt])
# a=v.write_videofile("k.mp4")

# c1.save_frame("text.jpg")
# c1.save_frame("text.jpg",t=3)

c1.audio.write_audiofile("extract.mp3")

au=c1.without_audio()
a=au.write_videofile("without_audio.mp4")
q=VideoFileClip("without_audio.mp4")
aud=AudioFileClip("extract.mp3")
clip_with_audio=q.set_audio(aud)
clip_with_audio.write_videofile("withsong.mp4")
