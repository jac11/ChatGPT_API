#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys ,time
import subprocess
from subprocess import PIPE
import json
import readline
for i in range(readline.get_current_history_length()):
    print (readline.get_history_item(i + 1))
    
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
    Check_Import ="pip show openai"
    Check_Import = subprocess.call(Check_Import,shell=True,stderr=subprocess.PIPE,stdout=PIPE) 
    if Check_Import == 0:
        pass
    else:
        os.system("pip3 install --upgrade requests >/dev/null 2>&1")
        Process = "pip install  openai"  
        subprocess.call(Process,shell=True,stderr=subprocess.PIPE,stdout=PIPE)   
                
class Chat_GPT:
    def __init__(self):
        self.__Connect_Openai()
    def __Connect_Openai(self):   
        import requests 
        import json
        with open("KEY_AI.json") as json_File:
            json_File = json.load(json_File)
            json_File = json_File["OPENAI_API_KEY"]
            openai_api_key = json_File    
            Bearer = "Bearer "+f"{openai_api_key}"  
            Back_end_api= "https://api.openai.com/v1/completions"
            Connect_Session = requests.Session() 
        def requests_Qury():
            prompt = input(R+"👨 USER     ---|  "+W).strip()
            if prompt == "EXIT".lower() or prompt=="exit".upper():
                print('[*] session is closed')
                exit()
            else:
                pass  
            if "code" in prompt:    
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
            if "code" in prompt:                
                with open ("code",'w') as f :
                    code =  f.write(str(response_text["choices"][0]["text"]))
                    return str(response_text["choices"][0]["text"]).replace('\n','')
            else:    
                return str(response_text["choices"][0]["text"]).replace('\n','')
        list1 = []
        while True  :
            reply = requests_Qury() 
            with open("./answer.txt",'w')as answer :
                if "." in reply[1] : 
                    reply = reply.split(".")
                    conut = 1
                    conut_ = 1
                    for line in reply :
                        try : 
                           replace = ''+line+'.'+reply[conut_]
                           conut +=1
                           conut_ +=1
                           if '.' in replace[1] or '.' in replace[2]:
                               list1.append(replace)                               
                        except IndexError:
                            break       
                    write = "\n".join(list1)        
                    Handdel = answer.write(write.strip())
                    list1= []
                elif '.' in reply and ',' in reply :
                   Handdel = answer.write(reply.replace('.','\n').replace(',','\n',2))                           
                else:
                    Handdel = answer.write(reply.replace('.','\n')) 
            with open("./answer.txt",'r') as read_answer:
                ReadData = read_answer.readlines()
                try:
                    if write:
                        print(Y+"🦾 ChatGPT  ---| "+W+B,end='')
                    else:
                        print(Y+"🦾 ChatGPT  ---|  "+W+B,end='')
                except UnboundLocalError:  
                        print(Y+"🦾 ChatGPT  ---|  "+W+B,end='')            
                for i in  ReadData[0]:
                    sys.stdout.write(i)
                    sys.stdout.flush()
                    time.sleep(3./90)  
                print("              ",end='')    
                ReadData = str("".join(ReadData[1:]))#  
                for i in ReadData : 
                     sys.stdout.write(i)
                     sys.stdout.flush()
                     time.sleep(3./90) 
                     if '\n' in i :
                        print("              ",end='')
                print("\n",end='')
if __name__=='__main__':
    #_Conections()
    #__Check_Import()
    Chat_GPT()             
