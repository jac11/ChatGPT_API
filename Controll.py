#!/usr/bin/env  python
from Chat_Package.ChatGpt import Chat_GPT
from Chat_Package.Banner import *
class Control:
    def __init__(self):
        self.Control_all()
    def Control_all(self):
        run = Banner_Logo()
        run = Chat_GPT()
if __name__=='__main__':
    Control()
