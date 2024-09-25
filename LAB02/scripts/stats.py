import os
import pandas as pd
import numpy as np

def calcular_estatisticas(diretorio, nome_arquivo, arquivo_saida):
    resultados = []
    for raiz, diretorios, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            if arquivo == nome_arquivo:
                caminho_completo = os.path.join(raiz, arquivo)

                if os.path.getsize(caminho_completo) <= 0:
                    continue
                
                df = pd.read_csv(caminho_completo)
                estatisticas = {}
                for coluna in ['cbo', 'dit', 'lcom', 'loc']:
                    if coluna in df.columns:
                        estatisticas = {
                            'coluna': coluna,
                            'mediana': df[coluna].median(),
                            'media': df[coluna].mean(),
                            'desvio_padrao': df[coluna].std()
                        }
                    else:
                        print(f"A coluna '{coluna}' não foi encontrada no arquivo {caminho_completo}")

                    resultados.append(estatisticas)

    
    df_resultados = pd.DataFrame(resultados)
    estatisticas_finais = df_resultados.groupby('coluna').agg(['mean', 'median', 'std'])
    estatisticas_finais.columns = estatisticas_finais.columns.droplevel()
    estatisticas_finais.to_csv(arquivo_saida)

calcular_estatisticas('/home/carlos/Documentos/faculdade/LES/LAB02/output/', 'class.csv', './stats_class.csv')
