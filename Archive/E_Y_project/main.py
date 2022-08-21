## Text to Speech
from mpyg321.MPyg123Player import MPyg123Player # or MPyg321Player if you installed mpg321

# source:  https://www.geeksforgeeks.org/convert-text-speech-python/ 

# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
mytext = "this is Emily's and Yaniv's first Projects as advencted python programmers!"
  
# Language in which you want to convert
language = 'en'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
  
# Playing the converted file
#os.system("mpg321 welcome.mp3")



# source : https://pypi.org/project/mpyg321/
player = MPyg123Player()
player.play_song("C:\Users\Mai\Desktop\Python\welcome.mp3")