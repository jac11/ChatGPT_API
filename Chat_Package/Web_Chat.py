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
import base64
python = "ls /usr/bin/python*"
reslut = subprocess.run(python,shell=True,capture_output=True)
reslut= str(reslut.stdout.decode()).split()[0][-7:]

if "--color-off" in sys.argv:
    W,R,B,Y ='','','',''   
elif "-C" in sys.argv:
    W,R,B,Y ='','','',''
else:  
    W,R,B,Y = '\033[0m','\033[1;31m','\033[1;34m' ,'\033[1;33m' 
#const API_KEY_64 = ""; // Paste your API key here
class Web_side :
    def __init__(self):
        Banner2_logo()
        self.unzip_web()
        self.Set_Web()
        self.Chech_Web_IN_Process()
    def unzip_web(self): 
        if os.path.exists("./Chat_Package/Web_Side"):
            pass
        else:    
            with ZipFile("./Chat_Package/Web_Side.zip",'r') as unzipweb :
                unzipweb.extractall(path='./Chat_Package/')
                os.remove('./Chat_Package/Web_Side.zip') 
            with open ("Chat_Package/.KEY_AI.json" ,'r') as Key_ai :
                 Key_ai = Key_ai.read().split(":")[1][2:-3]
            encoded_64 = str(base64.b64encode(Key_ai.encode())).replace("b'",'').replace("'",'')
            with open("Chat_Package/Web_Side/script.js",'r') as js:
               js = js.read().replace('const API_KEY_64 = ""; // Paste your API key here','const API_KEY_64 ="'+encoded_64+'"')
            with open("Chat_Package/Web_Side/script.js",'w') as jscript:
                jscript.write(js)   
    def Set_Web(self):            
        genrate_port = [num for num in range(5001,8000)]
        set_port = random.choice(genrate_port)
        with open('./Chat_Package/Web_Side/.port','w') as port:
            port.write(str(set_port))
        with open('./Chat_Package/Web_Side/.port','r')as readport :
            port =readport.read()
        Command = 'nohup '+reslut+' ./Chat_Package/Web_Side/server.py  >/dev/null 2>&1 & '
        print(R+'🌏 Web Chat server at  : ',Y+'http://127.0.0.1:'+port+"/Chat_Package/Web_Side/")
        os.system(Command) 
    def Chech_Web_IN_Process(self): 
        Process_ID = []
        web_port = []
        def Check_Browser():
            get_id = "lsof  | grep  python | grep LISTEN >.code "
            subprocess.call(get_id,shell=True,stderr=subprocess.PIPE,stdout=PIPE)
            with open('./.code','r') as output:
                    lsof = output.read().replace("python    ",'').replace("python3    ",'').replace("                        ",'-')
            with open(".code",'w') as data : 
                data.write(lsof)
            with open(".code",'r') as readdata:
                    readdata = readdata.read()
            rex_id = str("".join(re.findall('.+-',readdata))).split('-')
            rex_port = str("".join(re.findall(':\\d+',readdata))).split(":")[1:]
            for i in rex_id:
                Process_ID.append(i)
            for p in rex_port:
                web_port.append(p)    
        while True: 
            time.sleep(5)           
            test = subprocess.run(['ps -uax '],shell=True,capture_output=True)
            if "firefox" in test.stdout.decode():
               Check_Browser()
            else:
                break    
        for ID in Process_ID :
          kill_id = "kill -9 "+str(ID)
          subprocess.call(kill_id,shell=True,stderr=subprocess.PIPE,stdout=PIPE) 
        for port in web_port:
            kill_port = 'fuser -k  '+port+"/tcp >/dev/null 2>&1"
            os.system(kill_port) 
        print(R+"🚨️ Browser Status      :  "+B+"Browser Close")      
        time.sleep(.30)  
        print(R+"🚨️ Server Status       :  "+B+"Website down")
if __name__ == '__main__':
    Web_side()            
               
