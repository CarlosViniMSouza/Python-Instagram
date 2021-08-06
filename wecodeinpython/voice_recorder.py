# pip install sounddevice scipy

import sounddevice
from scipy.to.wavfile import write

fz = 44100

second = int(input("The time duration is: "))

print("Recording ... \n")

recording = sounddevice.rec(
    int(second * fz),
    sample_rate = fz,
    channels = 2,
)

sounddevice.wait()

write("Output Wav", fz, recording)

print("Finished ... \n Please Check it Recorder!")