
import moviepy.editor as mp
import time

start_time = time.time()

for i in range(1,6):
    video = mp.VideoFileClip(f"{i}.mp4")
    audio = video.audio
    audio.write_audiofile(f"{i}.mp3")

end_time = time.time()

print( end_time - start_time)
