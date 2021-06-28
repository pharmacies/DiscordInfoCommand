import discord
import os
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="EnterYourPrefix", case_insensitive=True, intents=intents)



@client.event
async def on_ready():
  await client.change_presence(status = discord.Status.online, activity = discord.Game(".help"))
  print("Bot is ready")
  
  
  
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

        

token = "Your bot Token"        

client.run(token)
