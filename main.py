import time
import ctypes
import os
from pypresence import Presence

def cls():
    os.system('cls')

#Declaring Variables incase user doesn't want images or buttons
large_img_key = "Breaks code if not included"
small_img_key = "Breaks code if not included"
url = "URL for button"
button_name = "Name of the button"
use_buttons = "if user wants buttons"
how_many_buttons = "How many buttons user wants"
url2 = "URL for button"
button_name2 = "Name of the button"

ctypes.windll.kernel32.SetConsoleTitleW("Discord RPC by Clumsy#0420")

use_large_imgs = input("Would you like to use large images Y/N? ").lower()
if use_large_imgs == "y":
    large_img_key = input("What's your image key? ").lower()

use_small_imgs = input("Would you like to use Small images Y/N? ").lower()
if use_small_imgs == "y":
    small_img_key = input("What's your image key? ")

use_buttons = input("Would you like to use buttons? Y/N? ").lower()
# how_many_buttons = input("How many buttons would you like? (limit = 2): ")
button_name = input("What would you like the button's name to be? ")
url = input("What website would you like to link? (MAKE SURE TO INCLUDE ENTIRE URL): ")
# if how_many_buttons == "2":
#     button_name2 = input("What would you like the second button's name to be? ")
#     url2 = input("What website would you like to link? (MAKE SURE TO INCLUDE ENTIRE URL): ")

What_Status = input("What Would you like your Status to say? ")
What_Description = input("What Would you like your description to say? ")
ClientID = input("Please input your Client ID: ").lower()

cls()

#Connecting to ClientID for RPC

RPC = Presence(ClientID)
RPC.connect()
print("Succesfully Connected to RPC")



RPC.update(large_image=large_img_key, small_image=small_img_key, buttons=[{"label": button_name, "url": url}], state=What_Status, details=What_Description)

while True:
    time.sleep(15) 

