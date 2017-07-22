# FkPyramids
Twitch bot coded in Python to automatically block pyramids after the third message

Twitch has an IRC server for chat that anyone is free to connect to. This script uses socket to connect to this IRC server, detects when someone is attempting a pyramid, and blocks it after the third stage.

## Requirements
* Python 3.5.x

## Setup
After cloning the repository or downloading FkPyramids.py, you need to enter your Twitch username in the Nick field, and your TMI key into the Pass field. To get your TMI key, [here](http://twitchapps.com/tmi)) and connect with your Twitch account. Optionally, you can replace "Channel = input("Channel: ")" to be a static selection.

## Running
`python3 FkPyramids.py` or run through a python IDE.
