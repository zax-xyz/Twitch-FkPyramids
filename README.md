# FkPyramids
Twitch bot coded in Python to automatically block pyramids after the third message

This script uses socket to connect to Twitch's chat IRC server, detects when someone is attempting a pyramid, and blocks it after the third stage.

## Requirements
* Python 3.6+

## Setup
* On line 11, replace `zaxu__` with your own Twitch username (keep it enclosed within the quotes), i.e. `'username'`
* Get an OAuth token from https://twitchapps.com/tmi/ using the bot's account.
* Create an `auth` file in the same directory with the bot's username and its OAuth token, separated by a space

## Running
### Windows
```
$ python FkPyramids.py
```

#### Linux/ Mac OS X
```
$ python3 FkPyramids.py
```
