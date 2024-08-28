import pandas as pd

def read_data_from_csv(path):
    data = pd.read_csv(path)
    return data

if __name__ == "__main__":
    data = read_data_from_csv("repos.csv")
    print(data)
