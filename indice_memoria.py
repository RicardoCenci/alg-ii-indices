import os
import math

APP_NAME = 0
APP_ID = 1
CATEGORY = 2
RATING = 3
RATING_COUNT = 4
INSTALLS = 5
MINIMUM_INSTALLS = 6
MAXIMUM_INSTALLS = 7
FREE = 8
PRICE = 9
CURRENCY = 10 
SIZE = 11
MINIMUM_ANDROID = 12
DEVELOPER_ID = 13
DEVELOPER_WEBSITE = 14
DEVELOPER_EMAIL = 15
RELEASED = 16
LAST_UPDATED = 17
CONTENT_RATING = 18
PRIVACY_POLICY = 19
AD_SUPPORTED = 20
IN_APP_PURCHASES = 21
EDITORS_CHOICE = 22
SCRAPED_TIM = 23


class HashIndice:
    def __init__(self, fileName):
        fileSize = os.path.getsize(fileName)
        self.fileName = fileName

        with open(fileName, 'rb') as f:
            line = f.readline().decode('utf-8')
            self.tamanhoRegistro = len(line)
            self.tamanho = math.floor(fileSize / self.tamanhoRegistro  * 0.20)
            self.buckets = [[] for _ in range(self.tamanho)]
            f.seek(0)

            while True:
                index = f.tell()
                registro = f.readline()
                
                if not registro:
                    break
                
                registro = registro.decode('utf-8').rstrip('\n').split(',')

                categoria = registro[CATEGORY].rstrip(' ')
                         
                self.inserir(categoria, index)

    def hash_funcao(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self.hash_funcao(chave)
        balde = self.buckets[indice]
        balde.append(valor)

    def findBucket(self, chave):
        indice = self.hash_funcao(chave)
        return self.buckets[indice]
        
    def find(self, chave):
        bucket = self.findBucket(chave)
        registers = []

        with open(self.fileName, 'rb') as f:
            for item in bucket:
                f.seek(item)
                registers.append(f.readline().decode('utf-8').rstrip('\n').split(','))

        return registers

            

indice = HashIndice('output.bin')
for item in indice.find('Tools'):
    print(item[APP_NAME])