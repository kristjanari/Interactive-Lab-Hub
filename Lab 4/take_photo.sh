
# from https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)
espeak -ven+f2 -k5 -s150 --stdout  "Congratulations! You win! Taking photo now" | aplay

numPhotos=$(ls photos | wc -l)

ffmpeg -f v4l2 -video_size 1280x720 -i /dev/video0 -frames 1 photos/"player$numPhotos.jpg"


espeak -ven+f2 -k5 -s150 --stdout  "Thank you! Photo saved! Have a good dayw" | aplay
