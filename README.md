# ChatGPT_API 
## Python Object - Terminal and Website Chat Interface -medule 3.5

*  Welcome to the ChatGPT_API Python Object README file! This Python Code  allows you to integrate the power of ChatGPT into both your terminal and website, providing a versatile conversational experience. The object offers three main options for interacting with ChatGPT:
 
-------------------------------------------------------------------------------------------------------------
## info about Openai
  * OpenAI is a pioneering organization in artificial intelligence research. Their mission is to ensure that artificial general intelligence (AGI) benefits all of humanity. ChatGPT is one of OpenAI's            remarkable creations, built upon the foundation of GPT (Generative Pre-trained Transformer) models.
  * ChatGPT is designed specifically for engaging in conversations. It can generate coherent and contextually relevant responses, making it an ideal candidate for chatbots, content creation, code assistance,    and more.
-----------------------------------------------------------------------------------------------------------------------
## Getting an API Key
*  Go to the OpenAI website and create an account.
*  log in to your account and go to the “API Keys” page.
*   Click the “Generate New API Key” button.
*   Enter a name for your key and click “Generate Key”.
*   Copy the generated API key and store it in a secure location.
*  Use the API key to access the OpenAI API.
*  You can get your OpenAI API key here: https://beta.openai.com/settings/developer
  ### Security Note
   * Keep your API key secure and never expose it publicly. Treat it like a password, as it provides access to the OpenAI services and resources.
    License
  * Feel free to contribute, report issues, and suggest enhancements on GitHub.
  * Feel free to adapt and expand upon this README according to your project's requirements. Be sure to replace placeholders like your-username and your-repo with your actual GitHub username and repository       name. If you have more questions or need further assistance, feel free to ask!
--------------------------------------------------------------------------------------------------------------------------
### required
### The ChatGPT_API will check for required packages and internet connection. It will install all the necessary packages in the background
  * ### Noted :-
    * Some errors can occur because permission to create folders and files is needed "to help ChatGPT_API function properly." So, run with sudo if it happens.   

*  ChatGPT_API along with a spelling tool to correct spelling errors strem in the chat session.
*  ChatGPT_API use requests python library to integrate with chatgpt openail
*  GNOME Shell  it required use to call aspell tool to fix spelling
*  dbus-x11 regureid th system call GNOME Shell
  
--------------------------------------------------------------------------------------------------------------------------
### OPtions
  * Terminal Chat (-T or --terminal): Engage in natural language conversations with ChatGPT directly from your terminal.Receive instant responses and make use of its language capabilities.

 * Website Chat Interface (-W or --chatweb): Communicate with ChatGPT through a website hosted on your local server using HTTP.Each time you use the website interface, the server will select a random available port. The server automatically closes when you close your browser.

 * Text Color Control (-C or --color-of): Customize the color of the displayed code text when using the terminal chat option. Choose from a variety of colors to enhance code readability.
---------------------------------------------------------------------------------------------------
## ChatGPT_API on Local Server 
* ChatGPT API on a local server. The unique aspect of this setup is that the server generates a random port each time it runs, and it will automatically close when you close your web browser. This allows you to interact with ChatGPT through a web-based interface in a secure and controlled environment.
## Note
* ### HTML CSS and JavaScript use in this porject get ready From Codingnepal
* [codingnepal](https://www.codingnepalweb.com/create-chatgpt-clone-html-css-javascript/)
* Thank you Codingnepal for support
----------------------------------------------------------------------------------------------
### Installation

To get started, follow these steps to install the ChatGPT_API :

 * git clone https://github.com/jac11/ChatGPT_API.git
 * cd ChatGPT_API
 * chmod +x chatgpt_api.py
 ------------------------------------------------------------------------------------------------------  
## Usage
* Engage in a conversation using the terminal chat option by running: --terminal or -T
  ```
  chatgpt_api --terminal
  chatgpt_api.py -T 
  ```
 * Start a local web server to access the ChatGPT website chat interfacee --webchat or -W
   ```
   chatgpt_api.py --webchat
   chatgpt_api -W
    ``` 
 * Supported colo Code Use : red, blue, yellow
 * if need to  ignore the color in the terminal chat   --color-off or -C
   ```
   chatgpt_api.py -C -T 
   ```
 
------------------------------------------------------------------------------------------------------------------------

## Connect Me :
* jac11devel@gmail.com
* Thank you 
  

