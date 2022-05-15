import numpy
import socket
import os
from Crypto.Random.random import getrandbits, randrange
def guess(s):
    C = 136
    N = 128
    K =  32
    numbers = []

    for i in range(N):
        nStr = ''
        for p in range(i):
            nStr = nStr + '0'
        nStr = nStr + '1'
        for p in range(N-i-1):
            nStr = nStr + '0'
        numbers.append(nStr)
    arr = numpy.full((8, 128), 0).tolist() #8 x 128 interleave array full of 0     
    j = 0
    for l0 in range(1):
        for l1 in range(2):
            for l2 in range(2):
                for l3 in range(2):
                    for l4 in range(2):
                        for l5 in range(2):
                            for l6 in range(2):
                                for l7 in range(2):
                                    arr[0][j] = 1 ##always 1, 000000000 is bo interesting
                                    arr[1][j] = l1
                                    arr[2][j] = l2
                                    arr[3][j] = l3
                                    arr[4][j] = l4
                                    arr[5][j] = l5
                                    arr[6][j] = l6
                                    arr[7][j] = l7
                                    j = j + 1
    for i in range(8):
        nStr = cleanAnswer(str(arr[i]))
        numbers.append(nStr)
    print("Open socket.")
    for k in range(K):
        print("Starting game ", k + 1, " of ", K)
        i = 1
        line = ''
        for n in numbers:
            nInt = int(n, 2)
            if k == 0:
                print(str(i)+" ==> "+n+" = "+str(nInt))
            s.sendall(bytes(str(nInt)+"\n", 'utf-8')) 
            line = line + cleanLight(readAnswer(s))
            i = i + 1
        while not "secret" in line:
            line = line + cleanLight(readAnswer(s))    
        print("All data send, expecting answer... : "+str(len(line)))
        line = cleanAnswer(line)
        print("Full :\n"+line)
        print("Number base :\n"+line[:128])
        print("Which bit is lying here is CRC MATRIX?")
        for i in range(8):
            nStr = cleanAnswer(str(arr[i]))
            print(nStr)
        crcBase = line[128:]
        print("\nCRC base :\n"+crcBase)

        print("Comparing CRC with former 128 responses")
        bitsOk = []
        for j in range(N):
            bitsOk.append(0)
        for i in range(8):
            baseBit = 0
            for j in range(N):
                if arr[i][j] == 1 and int(line[j]) == 1:
                    if baseBit == 0:
                        baseBit = 1
                    else:
                        baseBit = 0
            ## same base bit ?
            if baseBit == int(crcBase[i]):
                print("CRC ", i, "Ok ", baseBit)
                for j in range(N):
                    if arr[i][j] == 1:
                        bitsOk[j] = 1
            else:
                print("CRC ", i, "FAIL ", baseBit)
                for j in range(N):
                    if arr[i][j] == 0:
                        bitsOk[j] = 1

        print("BITS OK :\n"+cleanAnswer(str(bitsOk)))
        # toggle wrong bit
        print("Number base Before :\n"+line[:128])
        # should do a mask here but detail for debug understanding
        lineCRC = ''
        for j in range(N):
            if bitsOk[j] == 0:
                print("- CRC on col: ", j)
                if line[j] == '0':
                    lineCRC = lineCRC + '1'
                else:
                    lineCRC = lineCRC + '0'
            else:
                lineCRC = lineCRC + line[j]
        print("Number base after CRC :\n"+lineCRC)
        nInt = int(lineCRC, 2)
        print("Number : "+str(nInt))
        s.sendall(bytes(str(nInt)+"\n", 'utf-8')) 
        line = readAnswer(s)
        print(line)
        if "FCSC" in line:
            return True
    print("Completed : ")
    line = readAnswer(s)
    print(line)

    return False

def cleanLight(s):
    s = s.replace('>', '')
    s = s.replace(' ', '')
    return s

def cleanAnswer(s):
    s = cleanLight(s)
    s = s.replace('\n', '')
    s = s.replace('[', '')
    s = s.replace(']', '')
    s = s.replace(',', '')
    s = s.replace('Nowcanyouguessthesecret?', '')
    s = s.replace('Welldone!', '')
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
port = 2003

#host = "localhost"
#port = 3000

K =  32
count= 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, int(port)))
complete = guess(s)
while (not complete and count < K):
    count = count + 1
    print("attempt :", count)
    complete = guess(s)
#s.shutdown(socket.SHUT_WR)
#s.close()