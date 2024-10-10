import pandas as pd
import matplotlib.pyplot as plt

def ensure_type(pr):
    pr['changedFiles'] = pr['changedFiles'].astype(int)
    pr['additions'] = pr['additions'].astype(int)
    pr['deletions'] = pr['deletions'].astype(int)
    pr['participants'] = pr['participants'].astype(int)
    pr['comments'] = pr['comments'].astype(int)

    return pr

def save_plots_box(pr):
    pr['changedFiles'].plot.box()
    plt.savefig("../visualization/changedFilesBox")
    pr['additions'].plot.box()
    plt.savefig("../visualization/additionsBox")
    pr['deletions'].plot.box()
    plt.savefig("../visualization/deletionsBox")
    pr['participants'].plot.box()
    plt.savefig("../visualization/participantsBox")
    pr['comments'].plot.box()
    plt.savefig("../visualization/commentsBox")
    
def make_view():
    pr = pd.read_csv("../results/pr.csv")
    pr = ensure_type(pr)
    save_plots_box(pr)    

if __name__ == "__main__":
    make_view()
