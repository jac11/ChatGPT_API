#!/usr/bin/env python
import sys
import time
if "--color-off" in sys.argv:
    W,R,B,Y ,O ='','','','',''   
elif "-C" in sys.argv:
    W,R,B,Y,O ='','','','',''
else:  
    W,R,B,Y,O = '\033[0m','\033[1;31m','\033[1;34m' ,'\033[1;33m' , '\033[37m' 
     
def Banner_Logo():
      Banner1 = O+"""                                                                                                       
                                  Oxc;'....';cx0                  
                             .0d:'..............'cd0'             
                           0l'.........,cc,.........'l0.          
                        ;x,............lddl............,xc        
                      .x'...............ol...............'x.      
                     o;...........,cdkO0KK0Okdc'...........;x     
                    d...........c0WWWWWWWWWWWWWW0c...........k    
                   o..........,0WWWWWWWWWWWWWWWWWW0,..........d   
                  l..........;NWWWN000000000000NWWWN;..........o  
                 :...........XWWk;..............;kWWX...........c 
                 ;.........l0WWc...'..........'...cWW0l.........;.
                ;.........:0XWO..:dkxd;....;dxkd:..OWX0:.........:
                ;.........d0XWx.;kkkkkk'..,kkkkkk;.xWX0d.........;
                '.........o0XWx.,xkkkkx'..'xkkkkx,.xWX0o.........'
                ..........;0XWK..,looc'....'cool,..KWX0;..........
                ...........;OWWx..................xWWO;...........
                ............cWWWXd:'''''''''''':dXWWWc...........'
                .............0WWWWWWWWWWWWWWWWWWWWWW0............'
                 ............'OWWWWWWWWWWWWWWWWWWWWO'............ 
                 ..............:OWWWWWWWWWWWWWWWWO:.............. 
                  ...............':lodXXXXXXool:'...............  
                   ...........,:::::::KKKKKK:::::::,...........   
                    .......:ONWWWWWWWWWWWWWWWWWWWWWWNO:.......    
                     .....xWWWWWWWWWWWWWWWWWWWWWWWWWWWWx.....     
                       ..lWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWl..       
                         kWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWk.        
                           NWWWWWWWWWWWWWWWWWWWWWWWWWWW           
                              WWWWWWWWWWWWWWWWWWWWWW.             
                                  dWWWWWWWWWWWWx                  
                                       ;XX:\n\n""" 
    
      TEXT  = Y+"\t\t\t\t--Welcome To ChatGPT--\n"
      TEXT += "\t\t\t  --Base OF Model GPT-3.5 OpenAI--\n"
      TEXT +="\t\t\t --ChatGPT-Helpper done by jacsroty--\n\n"+W
      TEXT +=R+"\t\t"+"*"*54+'\n\n'+W
      sys.stdout.write(Banner1)
      sys.stdout.flush()
      for text in TEXT:
          sys.stdout.write(text)
          sys.stdout.flush()
          time.sleep(4./90) 
def Banner2_logo():
      Banner2 = """    
 
                 'lOKXXX0kc.                   
              'KM        xMOdxxo:'            
             xMo      ;oKM,      XNd          
         'o0NMW   .cOWd            KW'        
       'KN  :MX   M,     'l0Xkc.    NM        
      'MO   ;MN   M. .lOW.     NNkc.KM.                       
      KM.   ;MN   MKd    ,kc.     .MMM             ...                                                                 
      kM,   ;MN   M'       Moko'     MK         'd0NWMWN0d,               """+Y+"Chatgpt-3.5\t\t\t"+W+B+"""lNNNK.     ;NNd            
       MN.    :OccM.       M,  dWd   .MX      .OMWx:'.,c0MMk.                                          ;MMdMMx     ;MMx
        0Wd'      NO'    .oM,  oMK    MM      0MM;       oMMO  cXOo0NNXk,    :kXNNXk;   OXdxKNNKd.    .WMx oMMc    ;MMx
        WM.NXk:.   ,.dkxx  M,  oMK   .MK     .MMW        .MMW  oMMd,';kMMc .0MX,..lMMc  XMMc,,cWMX   .KMK.  0MM,   ;MMx 
        MM    .MKo:k0      M,  oMK  ,WN       XMM;       :MMO  oMM,    WM0 ,MMN0000NNx  XMM    KMM.  xMMWNNNNMMN.  ;MMx                                   
        .MO            .:xXx   xMWdKX         'XMWd;...,xMMk.  oMMo...oMMc .NMN;.   .   XMM    KMM. cMMo;;;;;oMMk  ;MMx                                   
          WXc.      ;xXM.      WM.              :kXMMMMWKx,    oMMXWMMW0:   .oKWWNXNX.  XMM    KMM.;MMO       kMMc ;MMx
            ,MN0OOXMW        :NW                   .....       oMM,....        .....    ...    ... ...         ...  ...
                    WXxl::lkNX                                 oMM,                                                   
                                                               .''.       """+Y+"""Terminal & web interface
                                                                             By-jacstory"""
                                                               
      print(B+Banner2+W)  
                                                                                                                                                                                 
                 