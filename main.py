import discord
from discord import CustomActivity
import asyncio
import os
import random
import json
import sys

time1 = 20 # Will send msg every 20 seocnds
presence = "Self bot | https://syntaxical.space" # Presence you want the account to have

ServerID = 1184110194905600132 # Server ID
ChannelID = 1213975152145072128 # Channel ID

# MAKE SURE THE ACCOUNT IS IN THE SERVER!

token = "" # Your discord token

# DONT EDIT UNLESS YOU KNOW WHAT YOUR DOING

def GetRandomMsg(): # Makes a fucntion
    try: # tries
        with open("index.json", "r") as f: # Reads index.json and exports the data as 'f'
            data = json.load(f) # Loads 'f'
            msgs = data["Messages"] # get the msgs data
            return random.choice(msgs) # Returns a random choice in the msgs array
    except FileNotFoundError: # If the file isnt found it will print \/
        print("FILE NOT FOUND | index.json")
    except (KeyError, json.JSONDecodeError) as e: 
        print(f"ERROR READING JSON: {e}")
        sys.exit(1)


class Myclient(discord.Client):
    async def on_ready(self): # WHen the bot is ready
        os.system('cls || clear') # clears terminal
        print("\033[1;96m", end="") # cyan text
        print("EXP Self bot | https://syntaxical.space") # Prints advertisemnet
        print("\033[0m", end="") # tells terminal to stop styling
        print(" \033[1;31m[*]\033[0m Press \"CTRL + C\" to stop the script.")   # normal red   
        print(f"This program will send the message a msg every {time1/60} Minutes!")

        channel = self.get_channel(ChannelID) # Retrieves channel

        await self.change_presence(activity=CustomActivity(name=presence, emoji="💫")) # Changes status to assert dominance
        while True: # Infinite loop
            msg = GetRandomMsg()
            await channel.send(msg) # Sends message to the selected channel
            print(f"Successfully sent! | MSG: {msg}") # Just making sure yk 
            await asyncio.sleep(time1) # Waits the selected tiem


client = Myclient() # Retrieves client (I think?)
client.run(token)
