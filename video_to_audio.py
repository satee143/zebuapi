import moviepy.editor
import os
os.chdir('/storage/emulated/0/Download')
# file location
video = moviepy.editor.VideoFileClip("a.mp4")
audio = video.audio
# video to audio conversion
audio.write_audiofile("out.mp3")