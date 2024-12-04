import pandas as pd
import glob

def concatena_csv(arquivos, arquivo_final):
    # Lista para armazenar todos os DataFrames
    dfs = []
    
    for arquivo in arquivos:
        # Lê cada arquivo CSV e adiciona na lista
        df = pd.read_csv(arquivo)
        dfs.append(df)
    
    # Concatena todos os DataFrames na lista em um único DataFrame
    df_final = pd.concat(dfs, ignore_index=True)

    # Salva o DataFrame final no arquivo de saída
    df_final.to_csv(arquivo_final, index=False)
    print(f"CSV concatenado com sucesso: {arquivo_final}")


# Lista de arquivos CSV a serem concatenados
arquivos = glob.glob('./*.csv')

# Nome do arquivo final
arquivo_final = "cuiaba-jan2023-nov2024.csv"

# Chama a função para concatenar os arquivos
concatena_csv(arquivos, arquivo_final)
