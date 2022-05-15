import socket
import os
def guess(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    i = 66 #prevent infinite
    print("Open socket.")
    numberL = 0
    numberH = int(18446744073709551615) # 8 bytes of 8 bits = int 64
    while True:
        number = numberL + int((numberH - numberL) / 2)# bug in round *? int((numberH + numberL) / 2)
     
        # print(str(i)+"==> "+str(number)+"      "+str(numberL)+ " - "+str(numberH)+" range = "+str(numberH - numberL))
        s.sendall(bytes(str(number)+"\n", 'utf-8')) 
        line=""
        while len(line) < 2:
            line = readAnswer(s)
            line = cleanAnwer(line)
        # print(line)

        if line.startswith("+1"):
            numberL = number + 1
        elif line.startswith("-1"):
            numberH = number - 1
        elif line.startswith("0"):
            numberL = 0
            numberH = int(18446744073709551615) # 8 bytes of 8 bits = int 64
            i = 66
            print(line)
        else:
            print(line)
        
        i = i - 1
        if i == 0:
            break
       
    s.shutdown(socket.SHUT_WR)
    s.close()
    return False

def cleanAnwer(s):
    s = s.replace(' ', '', 10)
    s = s.replace('>', '', 10)
    s = s.replace('\n', '', 10)
    return s

def getNumber(numberL, numberH):
    N = 64
    while (True):
        secret = int.from_bytes(os.urandom(N // 8), "big")
        if secret > numberL and secret < numberH:
            return secret

def readAnswer(s):
    data = s.recv(4096)
    clean = data.decode() # byte array to string
    return clean

host = "challenges.france-cybersecurity-challenge.fr"
port = 2001
complete = guess(host, port)
while not complete:
    complete = guess(host, port)
