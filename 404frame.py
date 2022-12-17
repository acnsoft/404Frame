#Created by AcnSoft - Arda Çalışkan
#github.com/acnsoft
#instagram.com/acnsoft


import socket
from api.telamonapi import *
from api.sqllookerapi import *

COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}


def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

bann = """




[[red]]$$\   $$\  $$$$$$\  $$\   $$\ $$$$$$$$\                 [[white]]                        
[[red]]$$ |  $$ |$$$ __$$\ $$ |  $$ |$$  _____|                       [[white]]                 
[[red]]$$ |  $$ |$$$$\ $$ |$$ |  $$ |$$ |    $$$$$$\  $$$$$$\  $$$$$$\$$$$\   $$$$$$\  [[white]]
[[red]]$$$$$$$$ |$$\$$\$$ |$$$$$$$$ |$$$$$\ $$  __$$\ \____$$\ $$  _$$  _$$\ $$  __$$\ [[white]]
[[red]]\_____$$ |$$ \$$$$ |\_____$$ |$$  __|$$ |  \__|$$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |[[white]]
[[red]]      $$ |$$ |\$$$ |      $$ |$$ |   $$ |     $$  __$$ |$$ | $$ | $$ |$$   ____|[[white]]
[[red]]      $$ |\$$$$$$  /      $$ |$$ |   $$ |     \$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\ [[white]]
[[red]]      \__| \______/       \__|\__|   \__|      \_______|\__| \__| \__| \_______|[[white]]
                                                                                
                                                                                    
"""

banner = colorText(bann)

redch = "[[red]]    >>>[[white]]"
redd = colorText(redch)

print(banner)
    
def portscann():
    telamon.scan(settarget , setportilnr)

def sqllook():
    sqllookerapi.sqllooker(settarget)

helpmenu = """
        
        Wellcome to 404 Frame Help Menu!

        set target: The “set target” command is a command that should be used independently of any attack. You introduce the target site to the system.

        set port: The port(s) you want to be scanned while the “set port” command is doing a port scan

        port scan: The “port scan” command checks the site you specified and whether the port(s) are open or closed.

        scan sql: The “scan sql” command will display all the results you have entered on the page that may have sql vulnerabilities.

        sets: The “sets” command will show you the target site – the port(s) you specified and other values ​​you entered. If you entered it incorrectly, you do not need to search.

        For more : https://acnsoft.net/404frame/

        ©️ 2022 AcnSoft. All rights reserved.
        """

while True:
    name = socket.gethostname()
    
    x = input(f"404frame@{name} >")
    

    #good commands

    if x == "help" or x == "menu" or  x == "help menu" or  x == "commands" or  x == "commands menu":
    
        print(helpmenu)

    if x == "set port":
        setportilnr = int(input(redd))
    
    if x == "set target":
        settarget = input(redd)
    
    if x == "sets":

        settings = f"""
        ---------------------------------------------------------
        [[white]]Target >>> [[red]]{settarget}[[white]]
        [[white]]Port >>> [[green]]{setportilnr}[[white]]      
        ---------------------------------------------------------  
        """
        
        setts = colorText(settings)
        print(setts)
    

    if x == "scan port":
        portscann()

    #sqllooker

    if x == "scan sql":
        sqllook()
