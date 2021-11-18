import time
import ctypes
import os
from colorama import Fore
from pypresence import Presence

def cls():
    os.system('cls')

#Declaring Variables incase user doesn't want images
large_img_key = "It breaks code if I don't declare a variable and the user doesn't want images"
small_img_key = "It breaks code if I don't declare a variable and the user doesn't want images"

ctypes.windll.kernel32.SetConsoleTitleW("Discord RPC by Clumsy#0420")

use_large_imgs = input("Would you like to use large images? Y/N? ").lower()
if use_large_imgs == "y":
    large_img_key = input("What's your image key? ").lower()
    
use_small_imgs = input("Would you like to use Small images? Y/N? ").lower()
if use_small_imgs == "y":
    small_img_key = input("What's your image key? ")

What_Status = input("What Would you like your Status to say? ")
What_Description = input("What Would you like your description to say? ")

ClientID = input("Please input your Client ID: ")

cls()

#Connecting to ClientID for RPC

RPC = Presence(ClientID)
RPC.connect()
print("Succesfully Connected to RPC")



RPC.update(large_image=large_img_key, small_image=small_img_key, state=What_Status, details=What_Description)

while True:
    time.sleep(15) 

