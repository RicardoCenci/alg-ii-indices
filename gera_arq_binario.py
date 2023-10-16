import csv

class CsvToBinaryFile:
    def __init__(self, csv_filename, bin_filename):
        self.csv_filename = csv_filename
        self.bin_filename = bin_filename
        self.column_sizes = self.get_column_sizes()

    def get_column_sizes(self):
        column_sizes = []
        with open(self.csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            column_sizes = [0] * len(next(csv_reader))
            for row in csv_reader:
                for i, value in enumerate(row):
                    size = len(value)
                    if size > column_sizes[i]:
                        column_sizes[i] = size
        return column_sizes

    def convert(self):
        with open(self.csv_filename, 'r', encoding='utf-8') as csv_file:
            with open(self.bin_filename, 'wb') as bin_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader) 
                for row in csv_reader:
                    formatted_row = []
                    for i, value in enumerate(row):
                        formatted_value = value.ljust(self.column_sizes[i])
                        formatted_row.append(formatted_value)
                    record = ','.join(formatted_row) + '\n'

                    bin_file.write(record.encode('utf-8'))

csv_to_bin = CsvToBinaryFile('Google-Playstore_slice_10000.csv', 'output.bin')
csv_to_bin.convert()