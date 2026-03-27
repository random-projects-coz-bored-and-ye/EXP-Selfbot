import discord
from discord import CustomActivity
import asyncio
import os
import random

time1 = 120 # Will send msg every 2 minutes
presence = "Self bot | https://syntaxical.space" # Presence you want the account to have

random_msgs = [
    "Hey guys! I wish you luck for the future!",
    "Good luck!",
    "Hey guys! How are you!",
    "How are you guys?",
    "Hope everyone has a great day!",
    "Wishing you all the best!",
    "Have a wonderful week ahead!",
    "What’s everyone up to?",
    "How’s it going today?",
    "Anyone watched something cool recently?",
    "Keep pushing forward!",
    "You all got this!",
    "Stay positive, team!",
    "Just dropping by to say hi!",
    "Who’s up for a challenge?",
    "Random thought: pizza is amazing.",
    "Hi everyone!",
    "Hello there!",
    "Good vibes to all!",
    "Hope you’re having a good one!",
    "Sending positive energy your way!",
    "Don’t forget to smile today!",
    "Take care, everyone!",
    "Keep grinding and shining!",
    "Hey hey! What’s up?",
    "Good morning, team!",
    "Good afternoon, folks!",
    "Good evening, friends!",
    "Stay awesome, everyone!",
    "ggs!",
    "bazinga!"
]


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
        print(f"This program will send the message a msg every {time1/60} Minutes!")

        channel = self.get_channel(ChannelID) # Retrieves channel

        await self.change_presence(activity=CustomActivity(name=presence, emoji="💫")) # Changes status to assert dominance
        while True: # Infinite loop
            msg = random.choice(random_msgs)
            await channel.send(msg) # Sends message to the selected channel
            print(f"Successfully sent! | MSG: {msg}") # Just making sure yk 
            await asyncio.sleep(time1) # Waits the selected tiem


client = Myclient() # Retrieves client (I think?)
client.run(token)


# Okay I think I fixed the issue where the msg gets deleted by adding like 30 msgs instead of 1
