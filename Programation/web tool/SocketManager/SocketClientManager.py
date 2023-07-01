from socket import *
import time


class SocketClientManager:
    def __init__(self, serverAdress, serverPort, isTCP=True):
        self.debugMode = False
        self._createSocket(isTCP)
        self._createConnection(serverAdress,serverPort)

    def _createSocket(self, isTCP):
        if isTCP:
            family = AF_INET
            type = SOCK_STREAM

        else:  # not isTCP
            family = AF_INET
            type = SOCK_DGRAM

        self.socket = socket(family, type)

    def _createConnection(self, serverAdress, serverPort):
        self.socket.connect((serverAdress, serverPort))

    def activateDebugMode(self):
        self.debugMode = True

    def desactivateDebugMode(self):
        self.debugMode = False

    def sendMessage(self, messageToSend):
        message = self._checkMessageToSend(messageToSend).encode()
        self.socket.send(message)

    def _checkMessageToSend(self, string):  # TODO
        checkedString = self._addJumpCaractere(self._cleanJumpCaractere(string))
        self._debugMessage("Message avant l'envoie (après nettoyage) :", checkedString)
        return checkedString

    @staticmethod
    def _cleanJumpCaractere(string):
        if string[-1] == "\n":
            string = string[:-1]
        return string

    @staticmethod
    def _addJumpCaractere(string):
        return string + " \n"

    def receiveMessage(self, bufferSize=2048, timeBeforeGetAnwser=0):
        if timeBeforeGetAnwser > 0:
            time.sleep(timeBeforeGetAnwser)
        message = self.socket.recv(bufferSize)
        self._debugMessage("Message reçu :", message)
        return message.decode()

    def close(self):
        self.socket.close()
        self.socket = None

    def _debugMessage(self, messageToProgrammer, info):
        if self.debugMode:
            print(messageToProgrammer, " ", info)
