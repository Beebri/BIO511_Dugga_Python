def histogram("brca_head500_genes.csv",fpkm_log2 ):
    import pandas as pd
    import matplotlib.pyplot as plt

    # Read the CSV file into a DataFrame
    df = pd.read_csv("brca_head500_genes.csv")

    # Plot histogram of the 'expression_level' column
    plt.hist(df['expression_level'], bins=30, color='blue', alpha=0.7)
    plt.title('Histogram of Gene Expression Levels')
    plt.xlabel('Expression Level')
    plt.ylabel('Frequency')
    plt.show()
