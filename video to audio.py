import moviepy.editor

# file location
video = moviepy.editor.VideoFileClip("video.mp4")
audio = video.audio
# video to audio conversion
audio.write_audiofile("out.mp3")
