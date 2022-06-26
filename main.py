import time
import json
from pypresence import Presence

with open("./Data/config.json") as f:
    config = json.load(f)

game = config.get('game')

if game == "phasmo":
    large_img_key = "logo"
    small_img_key = "steam"
    url = "https://store.steampowered.com/app/739630/Phasmophobia/"
    button_name = "Get Phasmopobia"
    ClientID = "913238116242948186"
    details = "Currently Ghost Huntin"
    status = "Why Not Join em!"
elif game == "bo3":
    large_img_key = "bo3"
    small_img_key = "logo"
    ClientID = "909565656549171272"
    button_name = "Get Black Ops 3"
    url = "https://store.steampowered.com/app/311210/Call_of_Duty_Black_Ops_III/"
    status = "Wanna kill em together?"
    details = "Curently Killin Zombies"
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

RPC = Presence(ClientID)
RPC.connect()
print("Succesfully Connected to RPC")

RPC.update(large_image=large_img_key, small_image=small_img_key,details=details, state=status, buttons=[{"label": button_name, "url": url}])

while True:
    time.sleep(15)