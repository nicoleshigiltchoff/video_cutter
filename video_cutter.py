from moviepy.editor import VideoFileClip
import os.path

full_video = "sample.mp4" #change this to your video name. must be an mp4.
clip_len = 59 #how long I want my parts, in seconds

#check if the file actually exists
if not os.path.isfile("./"+full_video):
    raise Exception(f"file {full_video} does not exist in the same directory as this python file")

name = full_video.split(".")[0]

full_len = VideoFileClip(full_video).duration
start_time = 0
clip_num = 1 

while True:
    if start_time >= full_len: #previous slice went to the end of the video
        print("Done slicing!")
        break
    
    end_time = start_time + clip_len

    #last video may be shorter
    if end_time > full_len:
        end_time = full_len

    clip = VideoFileClip(full_video).subclip(start_time, end_time)

    part_name = name+"_part_"+str(clip_num)+".mp4"
    clip.to_videofile(part_name, codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')
    clip_num += 1
    
    start_time = end_time # reset for next cut