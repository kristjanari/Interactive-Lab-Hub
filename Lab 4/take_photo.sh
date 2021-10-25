say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$*&tl=en"; }
#say $*
say "Congratulations! You win! Taking photo now"

numPhotos=$(ls photos | wc -l)

ffmpeg -f v4l2 -video_size 1280x720 -i /dev/video0 -frames 1 photos/"player$numPhotos.jpg"

say "Thank you! Photo saved! Have a good day."
say "Press the button to play again."
