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

class IndexedBinaryFile:
    def __init__(self, filename, index_filename):
        self.filename = filename
        self.index_filename = index_filename

    def convert(self):
        with open(self.filename, 'rb') as bin_file:
            with open(self.index_filename, 'wb') as index_file:
                while True:
                    pos = bin_file.tell()
                    record = bin_file.readline()

                    if not record:
                        break
                    
                    record = record.decode('utf-8').rstrip('\n').split('\,')
                    app_id = record[APP_ID]

                    index_file.write(f'{app_id},{pos}\n'.encode('utf-8'))

    def binary_search(self, target_app_id):
        with open(self.index_filename, 'r', encoding='utf-8') as f:
            esquerda = 0
            direita = 0

            while True:
                if not f.readline():
                    break
                direita += 1

        while esquerda <= direita:
            meio = (esquerda + direita) // 2

            with open(self.index_filename, 'r', encoding='utf-8') as f:
                for _ in range(meio):
                    next(f)
                linha = next(f).strip()
                app_id, posicao = linha.split(',')
                
                app_id = app_id.strip()

                if app_id == target_app_id:
                    with open(self.filename, 'r', encoding='utf-8') as f:
                        f.seek(int(posicao))
                        return [value.strip() for value in f.readline().rstrip('\n').split('\,')]
                elif app_id < target_app_id:
                    esquerda = meio + 1
                else:
                    direita = meio - 1

        return None

# Uso da classe
bin_file = IndexedBinaryFile('output.bin', 'index.txt')
bin_file.convert()

record = bin_file.binary_search('Sebha.pack')
print(record)