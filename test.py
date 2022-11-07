import speech_recognition as sr
from datetime import datetime

filename = datetime.now().strftime('%Y%m%d_%H:%M:%S')
txt =filename +".txt"

with open(txt, 'w') as f:
      f.write(filename + "\n")

r = sr.Recognizer()
mic = sr.Microphone()

while True:
      print("Say something ...")

      with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

      print ("Now to recognize it...")

      try:
            print(r.recognize_google(audio, language='ja-JP'))

            if r.recognize_google(audio, language='ja-JP') == "ストップ" :
                  print("end")
                  break
            with open(txt,'a') as f:
                  f.write("\n" + r.recognize_google(audio, language='ja-JP'))

      except sr.UnknownValueError:
            print("could not understand audio")
      except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
