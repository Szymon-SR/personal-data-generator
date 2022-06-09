import pandas as pd

CSV_PATH = 'results.csv'

def export_data_to_csv(list_of_rows):
    df = pd.DataFrame.from_dict(list_of_rows)
    df.to_csv(CSV_PATH, index=False, header=True)

    return CSV_PATH