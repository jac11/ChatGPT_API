#!/usr/bin/env  python
import os
import requests
from Chat_Package.ChatGpt import Chat_GPT
from Chat_Package.Banner import *

W='\033[0m'     
R='\033[1;31m'    
G='\033[0;32m'    
B='\033[1;34m' 
P='\033[35m'   
Y='\033[1;33m' 

class Control:
    def __init__(self):
        Chat_GPT._Conections(self)
        Chat_GPT._Check_Import(self)
        Check_key = os.listdir("./Chat_Package/")
        if ".KEY_AI.json" in Check_key :
            self.Control_all()
        else:  
            self._Input_Info()
    def _Input_Info(self):
        run =Banner2_logo()
        Info = R+"""\t\t\t    for first time run 
                            To add an API key to ChatGPT, you'll need to create an account on the ChatGPT website.
                            Once you've created an account, you'll be able to generate an API key which you can then add to the ChatGPT tool.
                            To do this, go to the Settings page, click the 'API Keys' tab, and click the 'Generate API Key' button.
                            Copy the generated API key and paste it into the ChatGPT tool."""+W
        Info += Y+"""\n\t\t\t\t\t\t\t\t\thttps://www.openai.com"""+W                    
        Info += R+"""\n\n\t\t\t\t\t\t***************************************************************\n"""+W

        for word in Info:          
            sys.stdout.write(word)
            sys.stdout.flush()
            time.sleep(4./90)       
        try:
            Input_Key = str(input(Y+"🌏 add the API KEY   : "+W)).strip()#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
        except :
            pass   
        with open('./Chat_Package/.KEY_AI.json','w') as APIKEY:
            APIKEY = APIKEY.write("{"+'\n'\
                +'  "OPENAI_API_KEY" '+' : '+'"'+Input_Key+'"'+'\n'\
                +"}")  
        def Test_API():
            with open('./Chat_Package/.KEY_AI.json','r') as APIKEY:
                 APIKEY = APIKEY.read().split(':')[1][2:-3]
            Back_end_api= "https://api.openai.com/v1/completions"
            response = requests.post(
                        Back_end_api,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer "+f"{APIKEY}",
                },
                json={
                    "prompt": 'Great Welcome',
                    "model": "text-davinci-003",
                    "max_tokens": 500,
                    "temperature": 0.5
                },
            ) 
            if response.status_code == 200:
               time.sleep(2)
               os.system('cls||clear')
               time.sleep(3)
               self.Control_all()
            else:
                from Chat_Package.Error_HTTP import Error_HTTP
                run = Error_HTTP(self)
                for Code,Error in self.HTTP_Error_Codes.items():
                    if str(response.status_code) == Code :
                        print(R+"⛔ Error API         :",APIKEY+'\n'+"⛔ API repones code  : "+Code+"-"+Error+W)                      
                        if os.path.exists('./Chat_Package/.KEY_AI.json'):
                           os.remove('./Chat_Package/.KEY_AI.json')
                           break
                        exit()    
        Test_API()                       
    def Control_all(self):
        run = Banner_Logo()
        run = Chat_GPT()
if __name__=='__main__':
    Control()
