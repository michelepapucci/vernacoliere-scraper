import pandas as pd

if __name__ == "__main__": 
    with open("data/title_list.txt", "w") as output_file:
        df = pd.read_csv("data/filtered_dataset.tsv", delimiter="\t")
        for index, row in df.iterrows():
            complete_title = row['title']
            if not pd.isna(df.iloc[index, 2]):
                complete_title += " " + str(row['subtitle'])
            output_file.write(complete_title + "\n")