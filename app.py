import tts, stt, AI
from multiprocessing import Process, Queue




if __name__ == '__main__':

    data = stt.learn()
    answer = AI.recognize(data)
    tts.speak(answer)