"""Script to add many last names from csv file"""

import csv

from names.models import LastName

MALE_FILENAME = (
    "/home/szymon/dev/personal_data_generator/data_generation/names/NAZWISKA_MĘSKIE.csv"
)
FEMALE_FILENAME = "/home/szymon/dev/personal_data_generator/data_generation/names/NAZWISKA_ŻEŃSKIE.csv"


def run():

    # clean the existing data in the database
    # LastName.objects.all().delete()

    # add from files to the database
    # to_database(MALE_FILENAME, True)
    # to_database(FEMALE_FILENAME, False)
    pass


def to_database(filename, picked_male_file):
    try:
        with open(filename) as file:
            reader = csv.reader(file)

            next(reader)  # skip the header

            for index, row in enumerate(reader):
                if index >= 10000:
                    break

                if not row[0].startswith("BRAK DANYCH"):
                    print(f"number {index}, {row[0]}")

                    # for female names, if the name already exists it means that it was added from male names
                    # this means that the name is gender - neutral and fits males and females
                    existing_obj = LastName.objects.filter(name=row[0]).first()

                    if existing_obj:
                        existing_obj.delete()
                        gender_letter = "N"
                    elif picked_male_file:
                        gender_letter = "M"
                    else:
                        gender_letter = "F"

                    new_name = LastName(name=row[0], matching_gender=gender_letter)

                    new_name.save()

        print("Finished importing from csv file to database")

    except FileNotFoundError:
        print(f"Failed to import data. File {filename} does not exist.")
