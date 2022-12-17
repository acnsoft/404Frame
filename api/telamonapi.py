#Created by AcnSoft - Arda Çalışkan
#github.com/acnsoft
#instagram.com/acnsoft

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class telamon():

    def scan(url , port):

        try:
            s.connect((url , port))
            print("[+] Port is OPEN>> "+str(port))
        except:
            print("[-] Port is CLOSED>> "+str(port))
