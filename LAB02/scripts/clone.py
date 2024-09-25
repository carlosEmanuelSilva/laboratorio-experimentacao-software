import pandas as pd
import os
import git

# Caminho para o arquivo CSV
csv_file = 'repos.csv'

# Pasta de destino para os clones
destino = 'repositorios_clonados'

# Carrega os dados do CSV
df = pd.read_csv(csv_file)

# Itera sobre cada linha do DataFrame
for index, row in df.iterrows():
    url_repositorio = row['url']  # Substitua 'URL' pelo nome da sua coluna de URLs
    nome_repositorio = url_repositorio.split('/')[-1].replace('.git', '')  # Extrai o nome do repositorio da URL

    # Cria o caminho completo para o clone
    caminho_clone = os.path.join(destino, nome_repositorio)

    try:
        # Clona o repositório
        git.Repo.clone_from(url_repositorio, caminho_clone)
        print(f"Repositório {nome_repositorio} clonado com sucesso!")
    except git.exc.GitCommandError as e:
        print(f"Erro ao clonar {nome_repositorio}: {e}")
