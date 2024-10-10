import pandas as pd

def get_stats(pr):
    print("Changed Files")
    print(pr['changedFiles'].describe())

    print("Additions")
    print(pr['additions'].describe())

    print("Deletions")
    print(pr['deletions'].describe())

    print("Participants")
    print(pr['participants'].describe())

    print("Comments")
    print(pr['comments'].describe())

def save_stats():
    pr = pd.read_csv("../results/pr.csv")
    get_stats(pr)

if __name__ == '__main__':
    save_stats()
