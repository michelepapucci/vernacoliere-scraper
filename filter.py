import pandas as pd
import numpy as np

if __name__ == "__main__":
    df = pd.read_csv("output.csv", delimiter= "\t")
    print(len(df))
    mask = df.drop(columns=['title']).isna().all(axis=1)
    filtered_df = df.drop(df[mask].index)
    print(len(filtered_df))
    filtered_df.to_csv("output_filtered.tsv", sep="\t", index=False)
    