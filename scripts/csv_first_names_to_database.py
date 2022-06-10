"""Script to add many first names from csv file"""

import csv

from names.models import FirstName

MALE_FILENAME = '/home/szymon/dev/personal_data_generator/data_generation/names/IMIONA_MĘSKIE.csv'
FEMALE_FILENAME = '/home/szymon/dev/personal_data_generator/data_generation/names/IMIONA_ŻEŃSKIE.csv'

def run():

    # clean the existing data in the database
    # FirstName.objects.all().delete()
    
    # add from files to the database
    to_database(MALE_FILENAME, True)
    to_database(FEMALE_FILENAME, False)
    pass


def to_database(filename, picked_male_file):
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            
            next(reader) # skip the header

            for index, row in enumerate(reader):
                if index > 100:
                    break

                print(f'number {index}, {row[0]}')                
                new_name = FirstName(name=row[0], is_male=picked_male_file)

                new_name.save()

        print('Finished importing from csv file to database')

    except FileNotFoundError:
        print(f'Failed to import data. File {filename} does not exist.')
