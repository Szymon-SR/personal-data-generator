"""Script to add many addreses from csv file"""

from addresses.models import PostAddress
import csv

CSV_FILENAME = "/home/szymon/dev/personal_data_generator/data_generation/addresses/input_addresses.csv"


def run():
    try:
        with open(CSV_FILENAME) as file:
            reader = csv.reader(file, delimiter=";")

            next(reader)  # skip the header

            # clean the existing data in the database
            # PostAddress.objects.all().delete()

            for row in reader:
                if not str(row[1]).startswith("Skrytki") and not str(row[1]).startswith(
                    "Instytucja"
                ):
                    print(row)

                    new_address = PostAddress(
                        city=row[2], post_code=row[0], voivodeship=row[3], county=row[4]
                    )
                    new_address.save()

        print("Finished importing from csv file to database")

    except FileNotFoundError:
        print(f"Failed to import data. File {CSV_FILENAME} does not exist.")
