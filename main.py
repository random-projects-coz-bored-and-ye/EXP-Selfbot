import discord
from discord import CustomActivity
import asyncio
import os

time1 = 120 # Will send msg every 2 minutes
msg = "Hey guys! I wish you luck for the future!" # msg to send every few minutes
presence = "Self bot | https://syntaxical.space" # Presence you want the account to have

ServerID = 1184110194905600132 # Server ID
ChannelID = 1213975152145072128 # Channel ID

# MAKE SURE THE ACCOUNT IS IN THE SERVER!

token = "" # Your discord token

# DONT EDIT UNLESS YOU KNOW WHAT YOUR DOING

class Myclient(discord.Client):
    async def on_ready(self): # WHen the bot is ready
        os.system('cls || clear') # clears terminal
        print("\033[1;96m", end="") # cyan text
        print("EXP Self bot | https://syntaxical.space") # Prints advertisemnet
        print("\033[0m", end="") # tells terminal to stop styling
        print(" \033[1;31m[*]\033[0m Press \"CTRL + C\" to stop the script.")   # normal red   
        print(f"This program will send the message {msg} every {time1/60} Minutes!")

        channel = self.get_channel(ChannelID) # Retrieves channel

        await self.change_presence(activity=CustomActivity(name=presence, emoji="💫")) # Changes status to assert dominance
        while True: # Infinite loop
            await channel.send(msg) # Sends message to the selected channel
            print("Successfully sent!") # Just making sure yk 
            await asyncio.sleep(time1) # Waits the selected tiem


client = Myclient() # Retrieves client (I think?)
client.run(token)

# HOLY DUB, WORKS FIRST TRY, DUBBBBBBBBBBBBBBBB
# NO AI, NO PRE-TESTING LETS FUCKING GOOOOOOOOOOOOOOOO
# I did use refrence code though (https://github.com/transicle/chess-stats.py/blob/main/client.py)

# Ez.gg
# Gotta upd syntaxical.space now but its ight
