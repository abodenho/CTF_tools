import os
import cv2

class UnPack:
    def __init__(self):
        self.answer = None
        self.isBase = False

    def unpack(self,name):
        extension = self.getExt(name)
        newName = self.getNewName(name,extension)

        if extension == "bz2":
            os.system("bzip2 -d " + name)

        elif extension == "xxd":
            self.commande("xxd -r " + name,newName)
        elif extension =="base64":

            self.commande("base64 -d " + name, newName)

        elif extension == "png":
            data = self.qrCodeReader(name)
            self.commande("echo "+data,newName)
        else:
            self.answer = True

        return newName


    def qrCodeReader(self,name):
        """ méthode qui lit un Qr code"""
        img = cv2.imread(name)
        detector = cv2.QRCodeDetector()
        data, bbox, straight_qrcode = detector.detectAndDecode(img)
        return data

    @staticmethod
    def commande(commande,newName):
        os.system(commande + " > " + newName)

    def getExt(self,name):
        longueur = len(name)-1
        extension = ""
        find = False
        while not find:
            if name[longueur] == ".":
                find = True
            else:
                extension = name[longueur] +extension
                longueur -=1

        return extension

    def getNewName(self,name,ext):
        longeurExt = len(ext)
        longeurName = len(name)
        return name[:longeurName-longeurExt-1]

    def getAnswer(self,file):
        fl = open(file+".txt","r")
        rep = None
        for line in fl:
            rep = line
            break
        return rep

a = UnPack()
name = "./UnPackMe.txt.base64.png.xxd.bz2.base64.xxd"
while(a.answer == None):
    name = a.unpack(name)

print(a.getAnswer(name))
