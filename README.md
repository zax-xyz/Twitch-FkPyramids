# FkPyramids
Twitch bot coded in Python to automatically block pyramids after the third message

This script uses socket to connect to Twitch's chat IRC server, detects when someone is attempting a pyramid, and blocks it after the third stage.

## Requirements
* Python 3.5.x

## Setup
Enter your Twitch username in the Nick field, and your TMI key into the Pass field. To get your TMI key, [here](http://twitchapps.com/tmi)) and connect with your Twitch account. Optionally, you can replace "Channel = input("Channel: ")" to be a static selection.

## Running
`python3 FkPyramids.py` or run through a python IDE.
