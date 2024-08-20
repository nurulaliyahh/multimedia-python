from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips
from moviepy.editor import vfx

video = VideoFileClip('avengers.mp4')
short_video = video.subclip(0, 10)  
combined_video = concatenate_videoclips([video, short_video])
reversed_video = short_video.fx(vfx.time_mirror)  
sped_up_video = short_video.fx(vfx.speedx, 2)  
sped_up_video.write_videofile('sped_up_result.mp4')