from PIL import Image
from PIL import ImageFilter
from pydub import AudioSegment

image = Image.open("anyaaa.jpg")


cropped_image = image.crop((10,10,200,200))

resized_image = cropped_image.resize((100,100))

filtered_image = resized_image.filter(ImageFilter.BLUR)

audio = AudioSegment.from_file('wakuwaku.mp3')

clipped_audio = audio[:10000]  

combined_audio = audio + clipped_audio

audio.export('result.wav', format='wav')

louder_audio = audio + 10  
louder_audio.export('louder_result.mp3', format='mp3')


