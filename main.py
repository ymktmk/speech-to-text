import glob
import pydub
import speech_recognition as sr
from datetime import datetime

r = sr.Recognizer()

# txtファイル
filename = datetime.now().strftime('%Y%m%d_%H:%M:%S')
txt =filename +".txt"
with open(txt, 'w') as f:
      f.write(filename + "\n")

# mp3変換
mp3_files = glob.glob('speech.mp3')
for mp3_file in mp3_files[:50]:
      sound = pydub.AudioSegment.from_mp3(mp3_file)
      sound.export(mp3_file.split("/")[-1][:-3] + "wav", format="wav")

# 文字起こし
wav_files = glob.glob('speech.wav')
for wav_file in wav_files[:10]: 
      with sr.AudioFile(wav_file) as source:
            audio = r.record(source)
      with open(txt,'a') as f:
            f.write("\n" + r.recognize_google(audio, language='ja-JP'))
