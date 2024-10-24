import pandas as pd
import matplotlib.pyplot as plt

def ensure_type(pr):
    pr['num_comments'] = pr['num_comments'].astype(int)
    pr['upvotes'] = pr['upvotes'].astype(int)
    pr['shares'] = pr['shares'].astype(int)
    pr['upvote_ratio'] = pr['upvote_ratio'].astype(int)

    return pr

def save_plots_box(pr):
    pr['num_comments'].plot.box()
    plt.savefig("../visualization/num_commentsBox")
    pr['upvotes'].plot.box()
    plt.savefig("../visualization/upvotesBox")
    pr['shares'].plot.box()
    plt.savefig("../visualization/sharesBox")
    pr['upvote_ratio'].plot.box()
    plt.savefig("../visualization/upvote_ratioBox")
    
def make_view():
    pr = pd.read_csv("../data/data1.csv")
    pr = ensure_type(pr)
    save_plots_box(pr)    

if __name__ == "__main__":
    make_view()
