#!/usr/bin/env python
import sys
import time
#climage --unicode --truecolor --cols 30  ip.png

W='\033[0m'     
R='\033[1;31m'    
G='\033[0;32m'    
B='\033[1;34m' 
P='\033[35m'   
Y='\033[1;33m' 
O='\33[37m'   

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
 
                        'o0NMMMMN0o,
                     :XM;        ,MNoodol;.
                    OMo        :xNM,     ,MNd.
                .cxKM0     'o0Md            xMk
              cXMl WMc   dWM.      .cc.      cMK
             KM;   NMc   NK     ;d0  ;MXx;    MM.
            XM:    NMc   N0 .cOMMx       NM0l,MM.                                                                                     
           .MM     NMc   NW0      dk:.      'MMM.       
            MM.    NMc   NK        oM.0d,     .MN.      # OpenAI ChatGPt-3.5
            cMX     .No' N0        cM   ;WO    .MW       
             .MNc       lMN.      .0M   .MM     MM;
              WMMW0l.       Ox;,oK xM   .MM     MM.
              MM.  ;MNx:   .oWx    cM   .MM    OMx
              WM:      OMKK       .KM   .MM  ;KM,
               MW;             ;xNMc    ,MM0WM.
                dMO;       .lOW0        XM;
                   0MX0OOKWMx         ;NM.
                           WWOl,'.,:xNM,
                                xO.     
      """
      print(B+Banner2+W)
                                                                                                                                                                                 
                                 
