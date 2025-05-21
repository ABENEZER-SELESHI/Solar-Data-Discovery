import pandas as pd
import os

def load_data():
    data_dir = "data"
    csv_files = [f for f in os.listdir(data_dir) if f.endswith(".csv")]

    dataframes = []
    for file in csv_files:
        df = pd.read_csv(os.path.join(data_dir, file))
        country_name = file.split("-")[0].capitalize()
        df["Country"] = country_name
        dataframes.append(df)

    combined_df = pd.concat(dataframes, ignore_index=True)
    
    if "Region" not in combined_df.columns:
        combined_df["Region"] = "West Africa"

    return combined_df

def get_top_regions(df, top_n=5):
    region_avg = df.groupby("Region")["GHI"].mean().sort_values(ascending=False).reset_index()
    region_avg.columns = ["Region", "Average GHI"]
    return region_avg.head(top_n)
