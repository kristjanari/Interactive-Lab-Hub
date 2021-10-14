# from https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)
espeak -ven+f2 -k5 -s150 --stdout  "What can I do for you today?" | aplay

#arecord -f cd -r 16000 -d 5 -t wav recorded.wav && sox recorded.wav recorded_mono.wav remix 1,2

arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_mono.wav
python3 speech.py recorded_mono.wav

espeak -ven+f2 -k5 -s150 --stdout  "Noted, is there aythig else I ca do for you?" | aplay

arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_mono.wav
python3 respond.py recorded_mono.wav

# from https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)
espeak -ven+f2 -k5 -s150 --stdout "All right, done!" | aplay

python3 server.py < output.txt

python butto.py
