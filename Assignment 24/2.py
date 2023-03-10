
import moviepy.editor as mp
from threading import Thread
import time

start_time = time.time()

def convert_video_to_audio(video_file, audio_file):
    video = mp.VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(audio_file)

threads = []

for i in range(1,2):
    t = Thread(target=convert_video_to_audio, args=(f"{i}.mp4", f"{i}.mp3"))
    threads.append(t)
    
for t in threads:
    t.start()
    
for t in threads:
    t.join()

end_time = time.time()

print( end_time - start_time)
