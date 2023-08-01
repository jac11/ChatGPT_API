#!/usr/bin/env python 
import os 
import random
path = os.getcwd()+'/Code_request/'
class Writer:
        def __init__(self):     
            self.write_Code()
        def write_Code(Self): 
            with open(os.getcwd()+'/Chat_Package/.Check_SPelling.txt','r') as order :        
                order = order.read().split()
            with open ("./Chat_Package/.Code_re.txt",'r') as code:
                  code = code.read()  
            Language_dic ={                                            
                              'powershell': '.ps1',
                              'css': '.css',
                              'html': '.html',
                              'assembly language': '.asm',
                              'c++': '.cpp',
                              'c': '.c',    
                              'c#': '.cs',
                              'java': '.java',
                              'javascript': '.js',
                              'objective-c': '.m',
                              'php': '.php',s
                              'perl': '.pl',
                              'python': '.py',
                              'ruby': '.rb',
                              'scala': '.scala',
                              'go': '.go',
                              'rust': '.rs',
                              'swift': '.swift',
                              'fortran': '.f',
                              'basic': '.bas',
                              'cobol': '.cbl',
                              'lisp': '.lisp',
                              'pascal': '.pas',
                              'pda': '.ada',
                              'erlang': '.erl',
                              'haskell': '.hs',
                              'prolog': '.pro',
                              'r': '.r',
                              'matlab': '.m',
                              'clojure': '.clj',
                              'f#': '.fs',
                              'julia': '.jl',
                              'vhdl': '.vhd',
                              'verilog': '.v',
                              'logo': '.logo',
                              'smalltalk': '.st',
                              'kotlin': '.kt',
                              'dart': '.dart',
                              'elixir': '.ex',
                              'groovy': '.groovy',
                              'haxe': '.hx',
                              'elm': '.elm',
                              'crystal': '.cr',
                              'bash':'.sh'
                       }          
            commants =  {
                              'python': '#',
                              'java': '//',
                              'c++': '//',
                              'c': '//',   
                              'javascript': '//',
                              'c#': '//',
                              'php': '//',
                              'r': '#',
                              'ruby': '#',
                              'perl': '#',
                              'go': '//',
                              'swift': '//',
                              'scala': '//',
                              'haskell': '--',
                              'objective-c': '//',
                              'rust': '//',
                              'matlab': '%',
                              'sql': '--',
                              'bash': '#',
                              'kotlin': '//',
                              'fortran': '!',
                              'julia': '#',
                              'groovy': '//',
                              'erlang': '%',
                              'lua': '--',
                              'clojure': ';',
                              'f#': '//',
                              'cobol': '*',
                              'pascal': '//',
                              'visual basic': '\'',
                              'ada': '--',
                              'prolog': '%',
                              'assembly': ';',
                              'apex': '//',
                              'vba': '\'',
                              'pl/sql': '--',
                              't-sql': '--',
                              'abap': '*',
                              'labview': '--',
                              'smalltalk': '"',
                              'xslt': '<!--',
                              'lisp': ';',
                              'dart': '//',
                              'css': '/* */',
                              'powershell': '#'
            }
            if os.path.exists('./Code_request/') : 
               pass
            else:            
               os.makedirs('./Code_request/')        
            for language,extension in Language_dic.items():  
               for lang in order :
                  if len(lang) == len(language): 
                     if language in order  and len(language) :
                        Count = [i for i in range(1,10001)]
                        Count  = random.choice(Count)
                        for lanC , commant in commants.items():
                           if language == lanC  :                        
                              with open(path+language+'_'+str(Count)+extension,'w') as Code_file:
                                 Coderequests = Code_file.write(str(commant)+"".join(order)+'\n'+code) 

if __name__=='__main__':
    Writer()