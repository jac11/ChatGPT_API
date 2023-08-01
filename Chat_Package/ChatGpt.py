#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys ,time
import subprocess
from subprocess import PIPE
import json
import readline
import signal
import threading
for i in range(readline.get_current_history_length()):
    print (readline.get_history_item(i + 1))
    print(readline.get_line_buffer())
    
W='\033[0m'     
R='\033[1;31m'    
G='\033[0;32m'    
B='\033[1;34m' 
P='\033[35m'   
Y='\033[1;33m' 

def _Conections():
    Check_Internet ='ping  -w1 www.google.com  >/dev/null 2>&1 '   
    communicate = os.system(Check_Internet)
    if communicate  == 0 :
        pass
    else:
        if communicate == 512:
            print("[+] No Internet Connection")
            exit()  
def __Check_Import ():  
    Check_Import ="pip show requests"
    Check_Import = subprocess.call(Check_Import,shell=True,stderr=subprocess.PIPE,stdout=PIPE) 
    if Check_Import == 0:
        pass
    else:
        os.system("pip3 install --upgrade requests >/dev/null 2>&1")
        Process = "pip install  requests"  
        subprocess.call(Process,shell=True,stderr=subprocess.PIPE,stdout=PIPE)   
                
class Chat_GPT:
    def __init__(self):
        self.__Connect_Openai()
    def __Connect_Openai(self):   
        import requests 
        import json
        with open("Chat_Package/.KEY_AI.json") as json_File:
            json_File = json.load(json_File)
            json_File = json_File["OPENAI_API_KEY"]
            openai_api_key = json_File    
            Bearer = "Bearer "+f"{openai_api_key}"  
            Back_end_api= "https://api.openai.com/v1/completions"
            Connect_Session = requests.Session() 
        def requests_Qury():
            prompt = input(R+"👨 USER     ---|  "+W).strip()
            with open("Chat_Package/.Check_SPelling.txt" ,'w')as Checker   :
                Checker.write(prompt) 
            SystemCall = subprocess.getstatusoutput('cat  Chat_Package/.Check_SPelling.txt | aspell --list')[1]
            if len(SystemCall) == 0 :
               pass
            else:  
                order2 = "aspell -c Chat_Package/.Check_SPelling.txt"
                command_proc3 = ' gnome-terminal --geometry 60x15+1000+60  -e ' +'"' + order2 +'"'  
                call_termminal = subprocess.call(command_proc3,shell=True,stderr=subprocess.PIPE) 
                while True:
                    Process = subprocess.getstatusoutput("ps ax | grep aspell | grep -v grep")[1]
                    if len(Process) != 0: 
                        sys.stdout.write('\x1b[1A')  
                        sys.stdout.write('\x1b[2K')
                        print(R+"👨 USER     ---|  "+W+str(prompt))
                    else:                
                        break   
                with open("Chat_Package/.Check_SPelling.txt" ,'r') as Checker :
                    prompt = Checker.read().strip()  
                    sys.stdout.write('\x1b[1A')  
                    sys.stdout.write('\x1b[2K')
                    print(R+"👨 USER     ---|  "+W+str(prompt))                                  
            if prompt == "EXIT".lower() or prompt=="exit".upper():
                print('[*] session is closed')
                exit()
            else:
                pass      
            if "code" in prompt:  
                from Chat_Package.Code_Writer import Writer  
                prompt_tittel =f'{prompt}'+" . Provide only code, no text",  
            else:
                prompt_tittel = prompt            
            response = Connect_Session.post(
                        Back_end_api,
                headers={
                    "Content-Type": "application/json",
                     "Authorization": f"{Bearer}",
                },
                json={
                    "prompt": prompt_tittel,
                    "model": "text-davinci-003",
                    "max_tokens": 500,
                    "temperature": 0.5
                },
            ) 
            response_text = json.loads(response.text)
            if "code" in prompt : 
                search = str(response_text["choices"][0]["text"])                     
                codeback = "\n".join(re.split("\\n\\n" ,search[2:]))                
                with open('Chat_Package/.Code_re.txt','w') as code_write:
                    coderwite =  code_write.write(codeback) 
                thread = threading.Thread(target=Writer)  
                thread.start()
                return  re.split("\\n\\n" ,search[2:]) 

            else:   
                search = str(response_text["choices"][0]["text"])          
                return  re.split("\\n\\n" ,search[2:])
        while True  :
            reply = requests_Qury()
            with open("Chat_Package/.answer.txt",'w')as answer :
                for i in reply:
                    try:
                       answer.write(i+'\n')
                    except :
                        pass       
            with open("Chat_Package/.answer.txt",'r') as read_answer:
                ReadData = read_answer.readlines()
                print(Y+"🦾 ChatGPT  ---|  "+W+B,end='')  
                C = 0
                for i in  ReadData[0]: 
                    if C == 100:
                        print("\n"+"\t\t  "+"-",end='') 
                        C = 0
                    sys.stdout.write(i)
                    sys.stdout.flush()
                    time.sleep(3./90)  
                    C +=1 
                print("\t\t  ",end='')  
                 
                ReadData = str("".join(ReadData[1:])) 
                C = 0
                for i in ReadData : 
                    if C == 100:
                        print("\n"+"\t\t  "+"-",end='') 
                        C = 0
                    sys.stdout.write(i)
                    sys.stdout.flush()
                    time.sleep(3./90) 
                    if '\n' in i :
                      print("\t\t  ",end='')
                print("\n",end='') 
if __name__=='__main__':
    _Conections()
    __Check_Import()
    Chat_GPT()             
