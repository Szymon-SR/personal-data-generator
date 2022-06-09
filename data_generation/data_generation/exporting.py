import pandas as pd

CSV_PATH = 'results.csv'
TXT_PATH = 'results.txt'


def export_data_to_csv(list_of_rows):
    df = pd.DataFrame.from_dict(list_of_rows)
    df.to_csv(CSV_PATH, index=False, header=True)

    return CSV_PATH


def export_data_to_txt(list_of_rows):
    df = pd.DataFrame.from_dict(list_of_rows)
    df_string = df.to_string(index=False, header=True)

    with open(TXT_PATH, 'a') as f:
        f.write(df_string)

    return TXT_PATH
