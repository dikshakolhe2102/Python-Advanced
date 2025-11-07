
from moviepy.editor import ImageClip

# Load an image and create a video clip from it
clip = ImageClip("output.png") 

# Set the duration of the clip (in seconds)
clip = clip.set_duration(5)

# Resize the image (optional)
from PIL import Image
if not hasattr(Image, 'ANTIALIAS'):
    Image.ANTIALIAS = Image.Resampling.LANCZOS
clip = clip.resize(width=640)  # Resize width to 640px, maintains aspect ratio

# Write the clip to a video file
clip.write_videofile("image_video.mkv",fps=24, codec="libx264")



