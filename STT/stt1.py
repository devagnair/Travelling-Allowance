import speech_recognition as sr
#import os
#from gtts import gTTS
from csv import writer
#import pandas as pd


r = sr.Recognizer()

li=[]
try:
  with sr.Microphone() as source1:
    print("Silence please, calibrating background noise")
    r.adjust_for_ambient_noise(source1,duration=2)
    print("Calibrated, now speak")
    print("From: ")
    From=r.listen(source1,phrase_time_limit=3)
    text=r.recognize_google(From)
    text=text.lower()
    print("You said: ",text)
    li.append(text)
  
    print("To: ")
    To=r.listen(source1,phrase_time_limit=3)
    text1=r.recognize_google(To)
    text1=text1.lower()
    print("You said: ",text1)
    li.append(text1)
except:
  print("Error in microphone")

print(li)
#print(text,text1)

# Open our existing CSV file in append mode
# Create a file object for this file
with open('journey.csv', 'a+',newline='') as f_object:
  
    # Pass this file object to csv.writer()
    # and get a writer object
    writer_object = writer(f_object)
  
    # Pass the list as an argument into
    # the writerow()
    writer_object.writerow(li)
  
    #Close the file object
    f_object.close()

print("\nSaved in File------!!!!!!")