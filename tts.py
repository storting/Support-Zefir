import torch, time
import sounddevice as sd


language = 'ru'
model_id = 'v3_1_ru'
sample_rate = 48000
speaker = 'eugene' #aidar, baya, kseniya, xenia, eugene, random
put_accent = True
put_yo = True
device = torch.device('cpu')

def speak(text):
    print("Говорю!")
    model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=language,
                                     speaker=model_id)
    model.to(device)  # gpu or cpu
    audio = model.apply_tts(text=text,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)

    print(text)
    sd.play(audio, sample_rate)
    time.sleep(len(audio)/sample_rate)
    sd.stop()

