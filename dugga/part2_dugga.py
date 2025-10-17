import csv
import pandas as pd
import matplotlib.pyplot as plt
import sys
#2.1
input_file = sys.argv[1]
df = pd.read_csv(input_file, sep=',')
print(df.head(30))
#2.2.1
def histogram(df):
    plt.hist(df["fpkm_log2"])
    plt.show()
histogram(df)
#2.2.2
"""run python part2_dugga.py brca_head500_genes.csv in terminal"""
#2.2.3
def histogram(df):
    plt.hist(df["fpkm_log2"])
    plt.title("Distribution of Gene Expression")
    plt.xlabel("Expression")
    plt.ylabel("Number of Genes")
    plt.savefig("fpkm_distribution.png")
histogram(df)