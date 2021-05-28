import threading
import webbrowser
from googlesearch import search
import time
import os

query = input("what to search ")

def gfg():
        time.sleep(1)                              
        os.system("TASKKILL /F /IM chrome.exe")

timer = threading.Timer(90.0, gfg) 
timer.start() 
webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("www.google.com/search?q=" + query)
for j in search(query, tld="co.in", num=2, start=0, stop=1, pause=4):
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(j)
