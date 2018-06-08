# FkPyramids
Twitch bot designed to automatically block pyramids after the third message

This script uses socket to connect to Twitch's chat IRC server, detects when someone is attempting a pyramid, and blocks it after the third message (or calls them out for doing a 2-tier pyramid which only lasts 3 messages).

This also commands with a command to automate its own pyramid within a fraction of a second which is nearly impossible to stop, along with other useless commands/functionality.

## Requirements
* Python 3.6+
* `termcolor` library

## Setup
* Create a second account on [Twitch](https://twitch.tv) for the bot to be run on, or use it on your own account (I'm assuming you already have your own primary account)
* On line 11, replace `zaxu__` with your own Twitch username (keep it enclosed within the quotes), i.e. `'username'`
* Get an OAuth token from https://twitchapps.com/tmi/ using the bot's account.
* Create an `auth` file in the same directory with the bot's username and its OAuth token, separated by a space

## Running
### Windows
```
$ python FkPyramids.py [channel]
```

#### Linux/ Mac OS X
```
$ python3 FkPyramids.py [channel]
```
Replace `[channel]` with the channel in which you wish the bot to be entered.
