# FkPyramids
Twitch bot coded in Python to automatically block pyramids after the third message

This script uses socket to connect to Twitch's chat IRC server, detects when someone is attempting a pyramid, and blocks it after the third stage.

## Requirements
* Python 3.5.x

## Setup
* On line 9, enter your Twitch username between the quotation marks
* On line 10, enter your Twitch TMI oauth key between the quotation marks ([twitchapps.com/tmi](http://twitchapps.com/tmi))
* On line 11, enter the Twitch channel you want to enter chat in between the quotation marks
* On line 76 (Twitch_Pyramid_Blocking) or line 62 (Full_Twitch_Bot.py), change "fkpyramids" to your Twitch bot's username (the same as what you put in line 9)

For Full_Twitch_Bot.py:
* On line 87, replace "zaxutic' with your own Twitch username

## Running
`python3 Twitch_Pyramid_Blocking.py` or `python3 Full_Twitch_Bot.py`
