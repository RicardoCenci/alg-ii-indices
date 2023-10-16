class IndexedBinaryFile:
    APP_NAME = 0

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
                    app_name = record[self.APP_NAME]
                    
                    index_file.write(f'{app_name},{pos}\n'.encode('utf-8'))
        
    def sort_index(self):
        with open(self.index_filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        self._merge_sort(lines, 0, len(lines) - 1)

        with open(self.index_filename, 'w', encoding='utf-8') as f:
            f.writelines(lines)

    def _merge_sort(self, lines, left, right):
        if left < right:
            middle = (left + right) // 2
            self._merge_sort(lines, left, middle)
            self._merge_sort(lines, middle + 1, right)
            self._merge(lines, left, middle, right)

    def _merge(self, lines, left, middle, right):
        left_half = lines[left:middle + 1]
        right_half = lines[middle + 1:right + 1]
        left_index = 0
        right_index = 0
        merge_index = left

        while left_index < len(left_half) and right_index < len(right_half):
            left_value = left_half[left_index].split(',')[0]
            right_value = right_half[right_index].split(',')[0]

            if left_value <= right_value:
                lines[merge_index] = left_half[left_index]
                left_index += 1
            else:
                lines[merge_index] = right_half[right_index]
                right_index += 1

            merge_index += 1

        while left_index < len(left_half):
            lines[merge_index] = left_half[left_index]
            left_index += 1
            merge_index += 1

        while right_index < len(right_half):
            lines[merge_index] = right_half[right_index]
            right_index += 1
            merge_index += 1

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

                if app_id.strip() == target_app_id:
                    with open(self.filename, 'r', encoding='utf-8') as f:
                        f.seek(int(posicao))
                        return [value.strip() for value in f.readline().rstrip('\n').split('\,')]
                elif app_id.strip() < target_app_id:
                    esquerda = meio + 1
                else:
                    direita = meio - 1

        return None

# Uso da classe
bin_file = IndexedBinaryFile('output.bin', 'index2.txt')
bin_file.convert()
bin_file.sort_index()

record = bin_file.binary_search('Turkey Clock')
print(record)