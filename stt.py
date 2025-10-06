import queue
import sys
import sounddevice as sd
import vosk
import json
import AI

model = vosk.Model("SpechModelSmall")
samplerate = 16000
device = 1

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def learn():
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device,
                dtype="int16", channels=1, callback=callback):
            rec = vosk.KaldiRecognizer(model, samplerate)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    data = json.loads(rec.Result())['text']
                    AI.recognize(data)
                #else:
                    #print(rec.PartialResult())