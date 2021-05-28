import discord
from discord.ext import commands
import random
import asyncio

TOKEN = 'ODMzODY1MzE5MzM1NzIzMDQ5.YH4jmA.cx9EXvhr8ctegoo2vwbWO5NXtA8'

client = discord.Client() #Since bots require a prefix, and we want DaBot to respond to random messages, use a client

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) #Prints a message in the terminal to signify bot is ready for use
    game = discord.Game("with myself, Let's Go!") #Set bot status
    await client.change_presence(status=discord.Status.online, activity=game)
    #Continue the loop forever
    while True:
        #In each server that the bot is connected to, scroll through each voice channel
        #The more servers it is connected to, the longer it will take for the bot to join back
        for guild in client.guilds: 
            for channel in guild.channels:
                await asyncio.sleep(1) #If there is no one connected to the voice channels at a given time, the bot will scroll through the channels too quickly and will not catch a user joining the channel if this pause is not implemented
                if isinstance(channel, discord.channel.VoiceChannel): #Check each channel to make sure it is a voice channel
                    member_ids = channel.voice_states.keys()
                    print(guild, channel, member_ids, sep=", ") 
                    if member_ids: #Do an initial check to see if call is occupied and queue triggering process
                        await asyncio.sleep(random.randint(900, 1200)) #The bot will randomly join the voice channel between 15 to 20 minutes
                        member_ids = channel.voice_states.keys() #After the 15-20 minutes participants could have left so check to see if occupants are still there
                        if member_ids:
                            vc = await channel.connect()
                            vc.play(discord.FFmpegPCMAudio(executable="C:/Program Files (x86)/FFmpeg for Audacity/ffmpeg.exe", source="audio.opus")) #Provide path to ffmpeg.exe file and audio source
                            await asyncio.sleep(3.5) #Wait until duration of audio clip and then dc
                            print("Audio successfuly played...")
                            await vc.disconnect()
                            await asyncio.sleep(120) # Wait 2 minutes in between cycles

@client.event
async def on_message(ctx):
    if ctx.author == client.user: #When a message is sent, make sure the bot did not send the message, if so ignore it
        return

    #Create an array that houses various gifs. The alternative to this is scraping giphy for the top gifs of a category
    gifs = ["https://media.giphy.com/media/kc0gID1xn99QDU9D1K/giphy.gif", "https://media.giphy.com/media/kBQLp6rWp0swtXnNaG/giphy.gif", "https://media.giphy.com/media/1BGPUWGTN9bMAbpxN6/giphy.gif", "https://media.giphy.com/media/fVcM5Nfk2S3tILoyEb/giphy.gif"] 
    if ctx.content.startswith(''): #On any message
        if random.randint(1, 100) == 1: #React on 1% of messages
            await ctx.channel.send("Let\'s Go!")
            await ctx.channel.send(random.choice(gifs)) #Send a random dababy gif from the list
   
client.run(TOKEN)


