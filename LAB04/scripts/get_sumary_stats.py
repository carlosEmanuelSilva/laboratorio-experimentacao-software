import pandas as pd

def get_stats(pr):
    print("num_comments")
    print(pr['num_comments'].describe())

    print("upvotes")
    print(pr['upvotes'].describe())

    print("shares")
    print(pr['shares'].describe())

    print("upvote_ratio")
    print(pr['upvote_ratio'].describe())


def save_stats():
    pr = pd.read_csv("../data/data1.csv")
    get_stats(pr)

if __name__ == '__main__':
    save_stats()
