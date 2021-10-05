#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import sys
import os
import wave
import json

if not os.path.exists("model"):
    print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit (1)

wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model("model")
# You can also specify the possible word list
rec = KaldiRecognizer(model, wf.getframerate(), "zero oh one two three four five six seven eight nine [unk]")

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        break
        print("string result: ")
        print(rec.Result())
        res = json.loads(str(rec.Result()))
        res2 = rec.Result().split("\n")
        print("the result: ")
        print(res2)
        print("jojo")
        #print(res["result"])
        f = open("output.txt", "w")
        f.write(rec.Result())
        f.close()
    else:
        print(rec.PartialResult())
print("ädjkdsjknksj")
resss = str(rec.FinalResult())
print(resss)
res = json.loads(resss)
print(res)
f = open("output.txt", "w")
f.write(res["text"])
f.close()
