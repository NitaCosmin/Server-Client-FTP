import socket 
import pathlib
from pathlib import Path


#importam functia pyftpdlib
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
#adresa
  
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)   
print("Numele calculatorului tau:"+hostname)   
print("Adresa ta IP:"+IPAddr)  
#server FTP creat cu adresa ip locala port default 21 pentru tarnsferul de fisiere
addr = (IPAddr,21) 
#path-ul catre fisierul de lucru
file=str(pathlib.Path().resolve())
print(file)
authorizer = DummyAuthorizer()
authorizer.add_user('Edy','12345',file,perm='elradfmwMT')
authorizer.add_user('Cosmin','12345',file,perm='elradfmwMT')
authorizer.add_user('Victor','12345',file,perm='elradfmwMT')

#adresa

handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(addr,handler)
server.serve_forever() 

