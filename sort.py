import pandas as pd
import sys

if len(sys.argv) != 3:
    print("Uso: python ordenar_csv.py arquivo.csv coluna")
    sys.exit(1)

nomeArquivo = sys.argv[1]
nomeColuna = sys.argv[2]

try:
    df = pd.read_csv(nomeArquivo)
except FileNotFoundError:
    print(f"Arquivo {nomeArquivo} não encontrado.")
    sys.exit(1)

if nomeColuna not in df.columns:
    print(f"A coluna {nomeColuna} não foi encontrada no arquivo CSV.")
    sys.exit(1)

df = df.sort_values(by=nomeColuna)
df.to_csv(nomeArquivo, index=False)

print(f"O arquivo {nomeArquivo} foi ordenado pela coluna {nomeColuna}.")
