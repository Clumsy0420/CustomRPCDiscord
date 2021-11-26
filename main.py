import time
import ctypes
import os
from pypresence import Presence

#Declaring Variables
small_img_key = None
url = None
button_name = None
ClientID = None
details = None
status = None
game = None

print("Black ops 3 = bo3")
print("Phasmopobia = phasmo")
print("Minecraft Java = java")
print("Minecraft Bedrock = bedrock")
print("Custom RPC = custom")
game = input("Which game RPC would you like: ").lower()
if game == "bo3":
    large_img_key = "bo3"
    small_img_key = "logo"
    ClientID = "909565656549171272"
    button_name = "Get Black Ops 3"
    url = "https://store.steampowered.com/app/311210/Call_of_Duty_Black_Ops_III/"
    status = "Wanna kill em together?"
    details = "Curently Killin Zombies"
elif game == "phasmo":
    large_img_key = "logo"
    small_img_key = "steam"
    url = "https://store.steampowered.com/app/739630/Phasmophobia/"
    button_name = "Get Phasmopobia"
    ClientID = "913238116242948186"
    details = "Currently Ghost Huntin"
    status = "Why Not Join em!"
elif game == "java":
    large_img_key = "java"
    small_img_key = "logo"
    url = "https://www.minecraft.net/en-us"
    button_name = "Get Minecraft Java"
    ClientID = "909912354622427186"
    details = "Slayin the Ender Dragon"
    status = "Wanna Join em?"
elif game == "bedrock":
    large_img_key = "game"
    small_img_key = "logo"
    url = "https://www.xbox.com/en-US/games/store/minecraft-for-windows/9nblggh2jhxj"
    button_name = "Get Minecraft Bedrock"
    ClientID = "837920143195111475"
    details = "Feeding the Bees"
    status = "Why not kill em?"
elif game == "custom":
    large_img_key = input("What's your large image key? ")
    small_img_key = input("What's your small image key? ")
    url = input("What would you like your buttons url to be? ")
    button_name = input ("What would you like your buttons name to be? ")
    details = input("What's your details? ")
    status = input("What's your status? ")
    ClientID = input("What's your client ID: ")
# Connecting to ClientID for RPC
RPC = Presence(ClientID)
RPC.connect()
print("Succesfully Connected to RPC")

RPC.update(large_image=large_img_key, small_image=small_img_key,details=details, state=status, buttons=[{"label": button_name, "url": url}])

while True:
    time.sleep(15)