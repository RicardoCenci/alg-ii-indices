import argparse
import pandas as pd

# py slice.py Google-Playstore 1000 
parser = argparse.ArgumentParser(description='Crie uma partição de um arquivo CSV.')
parser.add_argument('arquivo_csv', type=str, help='Nome do arquivo CSV de entrada')
parser.add_argument('linhas_por_particao', type=int, help='Número de linhas por partição')
args = parser.parse_args()

def criar_csv_de_saida(nome_arquivo_entrada, nome_arquivo_saida, num_linhas):
    try:
        df = pd.read_csv(nome_arquivo_entrada)
        df = df.head(num_linhas)
        df.to_csv(nome_arquivo_saida, index=False)
        print(f'{num_linhas} linhas do arquivo "{nome_arquivo_entrada}" foram salvas em "{nome_arquivo_saida}".')

    except FileNotFoundError:
        print(f'O arquivo "{nome_arquivo_entrada}" não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {str(e)}')

criar_csv_de_saida(
    f'{args.arquivo_csv}.csv',
    f'{args.arquivo_csv}_slice_{args.linhas_por_particao}.csv',
    args.linhas_por_particao
)