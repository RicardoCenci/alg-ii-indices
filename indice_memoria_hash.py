import os
import math
import csv_cols

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
                
                registro = registro.decode('utf-8').rstrip('\n').split('\,')

                categoria = registro[csv_cols.CATEGORY].rstrip(' ')
                         
                self.inserir(categoria, index)

    def _hash(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self._hash(chave)
        balde = self.buckets[indice]
        balde.append(valor)

    def findBucket(self, chave):
        indice = self._hash(chave)
        return self.buckets[indice]
        
    def find(self, chave):
        bucket = self.findBucket(chave)
        registers = []

        with open(self.fileName, 'rb') as f:
            for item in bucket:
                f.seek(item)
                registers.append(f.readline().decode('utf-8').rstrip('\n').split('\,'))

        return registers

            

indice = HashIndice('output.bin')
for item in indice.find('Tools'):
    print(item[csv_cols.APP_NAME])