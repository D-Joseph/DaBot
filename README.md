# DaBot
A meme Discord bot that checks if voice channels are populated, randomly joins, plays a DaBaby snippet, and leaves.  
Additionally, there is a 1% chance that the bot will respond to messages sent in the server "Let's Go!" and a GIF.

## How to Use
The bot's functionality is flexible, and can be applied to any sound that would make a group laugh when heard out of context. Simply swap the 'audio.opus' file (currently it is DaBaby's "Let's Go") for another and change the response to messages as appropriate!

## Required Tools
In order for the bot to work, you will need:
- The Discord library (`pip install discord.py`) 
  - Discord API provides bot's function
- ffmpeg.exe (https://ffmpeg.org/download.html)
  - Allows for the Discord API to play sounds
