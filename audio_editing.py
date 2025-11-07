
from moviepy.editor import AudioFileClip, concatenate_audioclips, CompositeAudioClip, afx
from moviepy.audio.fx.all import audio_fadein, audio_fadeout, volumex
from playsound import playsound   

 # Load two audio clips
audio1 = AudioFileClip("extract.mp3") 


# Play audio once (just load and preview duration)
print("Audio1 duration:", audio1.duration)
# playsound('extract.mp3')

#  Loop audio to a specific duration (e.g., 10 seconds) and saving the  audio

looped_audio = audio1.fx(afx.audio_loop, duration=50)
print("Looped audio duration:", looped_audio.duration)
# looped_audio.write_audiofile("looped_audio.mp3")

audio2 = AudioFileClip("looped_audio.mp3")
# #  Fade in and fade out (2 seconds each)
faded_audio = audio1.audio_fadein(5).audio_fadeout(5)
# faded_audio.write_audiofile("faded_audio.mp3")

# #  Adjust volume (reduce by 50%)
quieter_audio = audio1.volumex(1)
# quieter_audio.write_audiofile("quieter_audio.mp3")

# #  Concatenate audio clips sequentially
concat_audio = concatenate_audioclips([audio1, audio2])
# concat_audio.write_audiofile("concatenated_audio.mp3")

# #  Overlay audio clips (mix audio2 over audio1, starting audio2 at 3 seconds)
audio2_start = audio2.set_start(2)
composite_audio = CompositeAudioClip([audio1, audio2_start])
# composite_audio.write_audiofile("mixed_audio.mp3",fps=44100)

# #  Subclip (extract part from 2 to 4 seconds)
sub_audio = audio1.subclip(2, 4)
# sub_audio.write_audiofile("subclip_audio.mp3")

# # effects to audio 
# faded = audio1.fx(audio_fadein, 2).fx(audio_fadeout, 2)
# lowered = faded.fx(volumex, 0.3)
# lowered.write_audiofile("out_audio.mp3")