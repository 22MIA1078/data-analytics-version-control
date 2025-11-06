"""
Simple data cleaning script (sample).
Replace with your real project steps.
"""
import pandas as pd

def clean_data(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    # Example cleaning steps:
    # 1) Trim column names
    df.columns = [c.strip() for c in df.columns]
    # 2) Drop exact duplicate rows
    df = df.drop_duplicates()
    # 3) Handle missing values (example: fill numeric NA with median)
    for col in df.select_dtypes(include="number").columns:
        df[col] = df[col].fillna(df[col].median())
    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    print("Run: clean_data('raw.csv','clean.csv') in a Python shell")
