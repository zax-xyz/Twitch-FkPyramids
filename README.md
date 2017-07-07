# Twitch-Python-Pyramid-Blocking-Bot
Twitch bot coded in Python to automatically block pyramids after the third message

Twitch has an IRC server for chat that anyone is free to connect to. This script uses socket to connect to this IRC server. Along with automatically blocking pyramids, it also outputs messages received (but not its own that it sends to block pyramids).

## Requirements
To run this bot, you will need:
* Python 3.x

## Setup
After cloning the repository or downloading FkPyramids.py, you need to enter your Twitch username in the Nick field, and your TMI key into the Pass field. To get your TMI key, [here](http://twitchapps.com/tmi)) and connect with your Twitch account. Twitch IRC uses this key instead of the regular password for extra security. Optionally, you can replace "Channel = input("Channel: ")" to be a static selection, and have it automatically enter a specific channel everytime, for ease & convienence.

## Running
After setup, run FkPyramids.py with the command `<addr> python3 FkPyramids.py` or through your own python IDE.
