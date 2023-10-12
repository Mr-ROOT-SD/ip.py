import socket
import os
os.system ('clear')
print (''' 
      \033[0;31m ____  ____  ____  ______   _____ ____      
      / __ \/ __ \/ __ \/_  __/  / ___// __ \     
     / /_/ / / / / / / / / /     \__ \/ / / /     
    / _, _/ /_/ / /_/ / / /     ___/ / /_/ /      
   /_/ |_|\____/\____/ /_/     /____/_____/\033[0;31m       
                                          ''')
print ('\033[0;33mEnter you domain\033[0;33m:\033[0;36m ')
hostname=input()
ip=socket.gethostbyname(hostname)
print ('\033[0;34mhost name is\033[0;34m:\033[0;32m ',hostname, '\033[0;34mip is\033[0;34m: ' ,ip)
