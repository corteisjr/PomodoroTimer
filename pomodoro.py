import time
import wave
import os
import pyaudio
import sys

v = '\033[32m'
vv = '\033[0;0m'
# instantiate PyAudio (1)
def logo():
    print(v + """

 |  __ \                        | |                 |__   __(_)                    
 | |__) |__  _ __ ___   ___   __| | ___  _ __ ___      | |   _ _ __ ___   ___ _ __  |Criado por: Corteisjr
 |  ___/ _ \| '_ ` _ \ / _ \ / _` |/ _ \| '__/ _ \     | |  | | '_ ` _ \ / _ \ '__| |Contacto: +258840109913
 | |  | (_) | | | | | | (_) | (_| | (_) | | | (_) |    | |  | | | | | | |  __/ |    |Blog: Corteistech.blogspot.com
 |_|   \___/|_| |_| |_|\___/ \__,_|\___/|_|  \___/     |_|  |_|_| |_| |_|\___|_|   
                                                                                   
                                              
    """ + vv)
def audio():
    ficheiro = wave.open(r"./sound.wav","rb")
    p = pyaudio.PyAudio()

    # define callback (2)
    def callback(in_data, frame_count, time_info, status):
        data = ficheiro.readframes(frame_count)
        return (data, pyaudio.paContinue)

    # open stream using callback (3)
    stream = p.open(format=p.get_format_from_width(ficheiro.getsampwidth()),
                    channels=ficheiro.getnchannels(),
                    rate=ficheiro.getframerate(),
                    output=True,
                    stream_callback=callback)

    # start the stream (4)
    stream.start_stream()

    # wait for stream to finish (5)
    while stream.is_active():
        time.sleep(0.1)

    # stop stream (6)
    stream.stop_stream()
    stream.close()
    ficheiro.close()

    # close PyAudio (7)
    p.terminate()

def tempo():
    tempo = input("Digite os minutos ou (HH:MM:SS): ")
    if ":" in tempo:
        t_list = tempo.split(":")
        if len(t_list) == 2:
            t = float(t_list[0]) + \
                float(t_list[1])/60.0
        elif len(t_list) == 3:
            t = float(t_list[0]) * 60 + \
                float(t_list[1]) + \
                float(t_list[2]) / 60.0
        else:
            print("Error. Time format should be MM:SS or HH:MM:SS.")
            os.exit()
    else:
        t = eval(tempo)
    return t
def timer(times):
    secs_remaining = int(times - time.time())
    hours = secs_remaining // 3600
    minutes = (secs_remaining - hours * 3600) // 60
    seconds = secs_remaining - hours * 3600 - minutes * 60
    return "{0:2s}:{1:2s}:{2:2s}".format(str(hours).zfill(2), str(minutes).zfill(2), str(seconds).zfill(2))

def loop(times):
    while time.time() < times - 1:
        os.system("clear")
        print(timer(times))
        time.sleep(1)
def main():
    t = tempo()
    times = time.time() + t*60 + 1
    loop(times)
    os.system("clear")
    lo = logo()
    print("00:00:00")
    time.sleep(2)
    print('\033[31m'+"\n\nSe nao decides tuas prioridades\n e quanto tempo dedicaras a elas, alguem decidira por ti!\n\n"+ '\033[0;0m')
    audio()

if __name__ == "__main__":
    main()