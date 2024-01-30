from itertools import cycle
import time
import json
from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
from colorama import Fore, Style
import time
import random, os, requests, json
from requests_toolbelt.multipart.encoder import MultipartEncoder
import os
from os import system
from discord.ext import commands
from selenium import webdriver
from pathlib import Path
from tkinter import Tk, Canvas, END, Text, Button, PhotoImage,messagebox
import requests
import sys


def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(.1)

temp = os.getenv("temp")


def promote():
    
    def main():
        h = open('message.txt','r',encoding='utf-8')
        mes = h.read()

    h = open('message.txt','r',encoding='utf-8')
    mes = h.read()
    count = 0

    with open('config.json') as f:
        config = json.load(f)
        TOKEN = config.get('token')
        pmdelay = config.get('delay1')
        jmdelay = config.get('delay2')
        chaid1 = config.get('channel_id1')
        chaid2 = config.get('channel_id2')
        chaid3 = config.get('channel_id3')
        chaid4 = config.get('channel_id4')
        chaid5 = config.get('channel_id5')
        chaid6 = config.get('channel_id6')
        chaid7 = config.get('channel_id7')
        chaid8 = config.get('channel_id8')
        chaid9 = config.get('channel_id9')
        chaid10 = config.get('channel_id10')
        chaid11 = config.get('channel_id11')
        chaid12 = config.get('channel_id12')
        chaid13 = config.get('channel_id13')
        chaid14 = config.get('channel_id14')
        chaid15 = config.get('channel_id15')
        chaid16 = config.get('channel_id16')
        chaid17 = config.get('channel_id17')
        chaid18 = config.get('channel_id18')
        chaid19 = config.get('channel_id19')
        chaid20 = config.get('channel_id20')
        total = 0
        def countdown(t):
                while t:
                    mins, secs = divmod(t, 60)
                    timer = '{:02d}:{:02d}'.format(mins, secs)
        
                    print(f"Promote In : {timer}", end="\r")
                    time.sleep(1)
                    t -= 1

        def get_connection(): 
                return HTTPSConnection("discordapp.com", 443) 

        def send_message(conn, channel_id, message_data):
                try: 
                    conn.request("POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data) 
                    resp = conn.getresponse() 
                    
                    if 199 < resp.status < 300: 
                        print(Fore.LIGHTCYAN_EX + f"[+] Promote Auto : {total}\n")
                        pass 
            
                    else: 
                        stderr.write(Fore.LIGHTRED_EX + f"[!] Error: {resp.reason}\n")
                        pass 
            
                except: 
                    stderr.write(Fore.LIGHTRED_EX + f"[!] Error\n") 
            
        def main(): 
                message_data = { 
                    "content": mes, 
                    "tts": "false", 
                }
                send_message(get_connection(), chaid1, dumps(message_data))
                send_message(get_connection(), chaid2, dumps(message_data))
                send_message(get_connection(), chaid3, dumps(message_data))
                send_message(get_connection(), chaid3, dumps(message_data))
                send_message(get_connection(), chaid4, dumps(message_data))
                send_message(get_connection(), chaid5, dumps(message_data))
                send_message(get_connection(), chaid6, dumps(message_data))
                send_message(get_connection(), chaid7, dumps(message_data))
                send_message(get_connection(), chaid8, dumps(message_data))
                send_message(get_connection(), chaid9, dumps(message_data))
                send_message(get_connection(), chaid10, dumps(message_data))
                send_message(get_connection(), chaid11, dumps(message_data))
                send_message(get_connection(), chaid12, dumps(message_data))
                send_message(get_connection(), chaid13, dumps(message_data))
                send_message(get_connection(), chaid14, dumps(message_data))
                send_message(get_connection(), chaid15, dumps(message_data))
                send_message(get_connection(), chaid16, dumps(message_data))
                send_message(get_connection(), chaid17, dumps(message_data))
                send_message(get_connection(), chaid18, dumps(message_data))
                send_message(get_connection(), chaid19, dumps(message_data))
                send_message(get_connection(), chaid20, dumps(message_data))
        system('cls')

        h = open('message.txt','r',encoding='utf-8')
        mes = h.read()

        for i in range(2):
                system('cls')
                time.sleep(0.2)
                
        lockreasl = r"""

        time.sleep(0.2)
        system('cls')
        print("Wait for Checking...")
        time.sleep(2)
        header_data = { 
                "content-type": "application/json", 
                "user-agent": "discordapp.com", 
                "authorization": TOKEN, 
                "host": "discordapp.com"
        } 
        for i in range(10000):
            total = int(total + 1)
            main()
            system("title " + f"Channel : {chaid1} │ Delay Promote │ Promote : {total}")
            countdown(int(jmdelay))
    
    if __name__ == "__main__":
        main()
promote()