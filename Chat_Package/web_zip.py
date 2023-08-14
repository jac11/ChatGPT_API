#!/usr/bin/env python
import os,signal
import random
import time
import subprocess
from subprocess import PIPE,Popen,check_output
from zipfile import ZipFile


class Web_side :
    def __init__(self):
       #self.unzip_web()
        self.Set_Web()
        self.Chech_Web_IN_Process()
    def unzip_web(self): 
        with ZipFile("./Chat_Package/web_chat.zip",'r') as unzipweb :
            unzipweb.extractall(path='./Chat_Package/')
    def Set_Web(self):    
        genrate_port = [num for num in range(5001,8000)]
        set_port = random.choice(genrate_port)
        with open('./Chat_Package/Chat_Web/.port','w') as port:
            port.write(str(set_port))
        with open('./Chat_Package/Chat_Web/.port','r')as readport :
            port =readport.read()
        Command = 'nohup python ./Chat_Package/Chat_Web/server.py  >/dev/null 2>&1 & '
        print('🌏 Web Chat server at : http://127.0.0.1:'+str(port))
        os.system(Command) 
    def Chech_Web_IN_Process(self): 
        while True :
            if os.system('ps -A | grep firefox') == 0:
               print('Browser is open')
            else:
                print('Browser is closed') 
            time.sleep(3)       
if __name__ == '__main__':
    Web_side()            
               
