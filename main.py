import bisect

class BinaryFile:
    def __init__(self, filename):
        self.filename = filename
        self.record_size = 0;
        self.records = []
        self.load_records()

    def load_records(self):
        with open(self.filename, 'rb') as f:
            self.record_size = len(f.readline())

            while True:
                record = f.read(self.record_size)
                if not record:
                    break
                self.records.append(record)

    def insert_record(self, record):
        # Encontra a posição de inserção para manter a ordem
        pos = bisect.bisect_left(self.records, record)
        # Insere o registro na lista em memória
        self.records.insert(pos, record)
        # Reescreve o arquivo com os registros ordenados
        with open(self.filename, 'wb') as f:
            for record in self.records:
                f.write(record)

    def binary_search(self, key):
        # Converte a chave para bytes e preenche com espaços em branco se necessário
        key = key.encode().ljust(self.record_size)
        # Realiza a pesquisa binária na lista de registros
        pos = bisect.bisect_left(self.records, key)
        if pos != len(self.records) and self.records[pos] == key:
            return pos
        else:
            return -1

# Uso da classe
bin_file = BinaryFile('output.bin')
bin_file.insert_record('App ID')
pos = bin_file.binary_search('App ID')

if pos != -1:
    print(f'Record found at position {pos}')
else:
    print('Record not found')