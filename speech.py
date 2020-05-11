import speech_recognition as sr
import wave 
import sys

def Voice_To_Text():
    Text=''
    with sr.WavFile('test.wav') as source: #0~265
        # audio = r.record(source, offset=210, duration=30)
        # Text=r.recognize_google(audio, language="Zh-TW")
        r = sr.Recognizer()
        r.energy_threshold = 8000
        audio = r.record(source, duration=50)
        try:
            Text+=r.recognize_google(audio, language="Zh-TW")+"\n"
        except sr.UnknownValueError:
              Text += "無法翻譯"+"\n"
      
    return Text

#print(sr.__version__)
Text = Voice_To_Text()

with open("data.txt", mode="a", encoding="utf-8") as file:
    file.write(Text)