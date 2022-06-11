"""Exporting personal data to files"""

import typing
import pandas as pd


class FileExporter:
    """A class used to export data to different types of files"""

    BASE_PATH = "outputs/"
    CSV_PATH = f"{BASE_PATH}results.csv"
    TXT_PATH = f"{BASE_PATH}results.txt"
    XLSX_PATH = f"{BASE_PATH}results.xlsx"

    def __init__(self, list_of_rows: typing.List) -> None:
        self.list_of_rows = list_of_rows
        # initially create a pandas dataframe with all the data
        self.df = pd.DataFrame.from_dict(self.list_of_rows)

    def export_data_to_csv(self):
        """Create a csv file from dataframe, return the path to this file"""
        self.df.to_csv(FileExporter.CSV_PATH, index=False, header=True)

        return FileExporter.CSV_PATH

    def export_data_to_txt(self):
        """Create a txt file from dataframe, return the path to this file"""

        df_string = self.df.to_string(index=False, header=True)

        with open(FileExporter.TXT_PATH, "w") as f:
            f.write(df_string)

        return FileExporter.TXT_PATH

    def export_data_to_excel(self):
        """Create an excel (xlsx) file from dataframe, return the path to this file"""

        self.df.to_excel(
            FileExporter.XLSX_PATH, sheet_name="Generated", index=False, header=True
        )

        return FileExporter.XLSX_PATH
