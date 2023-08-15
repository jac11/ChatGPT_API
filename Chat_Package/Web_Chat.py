#!/usr/bin/env python
import os
import random
import time
import subprocess
from Chat_Package.Banner import Banner2_logo
from subprocess import PIPE,Popen,check_output
from zipfile import ZipFile
import sys
import re

if "--color-off" in sys.argv:
    W,R,B,Y ='','','',''   
elif "-C" in sys.argv:
    W,R,B,Y ='','','',''
else:  
    W,R,B,Y = '\033[0m','\033[1;31m','\033[1;34m' ,'\033[1;33m' 

class Web_side :
    def __init__(self):
        Banner2_logo()
        self.unzip_web()
        self.Set_Web()
        self.Chech_Web_IN_Process()
    def unzip_web(self): 
        if os.path.exists("./Chat_Package/Chat_Web"):
            pass
        else:    
            with ZipFile("./Chat_Package/Web_Side.zip",'r') as unzipweb :
                unzipweb.extractall(path='./Chat_Package/')
        #       os.remove('./Chat_Package/Web_Side.zip') 
    def Set_Web(self):    
        genrate_port = [num for num in range(5001,8000)]
        set_port = random.choice(genrate_port)
        with open('./Chat_Package/Chat_Web/.port','w') as port:
            port.write(str(set_port))
        with open('./Chat_Package/Chat_Web/.port','r')as readport :
            port =readport.read()
        Command = 'nohup python ./Chat_Package/Chat_Web/server.py  >/dev/null 2>&1 & '
        print(R+'🌏 Web Chat server at :',Y+'http://127.0.0.1:'+port+"/Chat_Package/Chat_Web/")
        os.system(Command) 
    def Chech_Web_IN_Process(self): 
        while True :
            if os.system('ps -A | grep firefox >/dev/null 2>&1') == 0:
              continue
            else:
                listIDS = []
                get_id = "lsof  | grep  python | grep LISTEN >.code "
                subprocess.call(get_id,shell=True,stderr=subprocess.PIPE,stdout=PIPE)
                with open('./.code','r') as output:
                    lsof = output.read().replace("python    ",'').replace("python3    ",'').replace("                        ",'-')
                with open(".code",'w') as data : 
                    data.write(lsof)
                with open(".code",'r') as readdata:
                     readdata = readdata.read()
                rex = str("".join(re.findall('.+-',readdata))).split('-')
                for ID in rex:
                    kill_id = "kill -9 "+ID
                    subprocess.call(kill_id,shell=True,stderr=subprocess.PIPE,stdout=PIPE)           
                print('Browser is closed') 
                exit()
            time.sleep(3)       
if __name__ == '__main__':
    Web_side()            
               
