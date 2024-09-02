import pandas as pd

def read_data_from_csv(path):
    data = pd.read_csv(path)
    data['create_date'] = pd.to_datetime(data['create_date']).dt.year
    data.to_csv('new_repos_file.csv', index=False)

if __name__ == "__main__":
    read_data_from_csv("repos.csv")
    print('Alterado')
