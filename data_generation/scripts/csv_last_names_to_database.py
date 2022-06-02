"""Script to add many street names from csv file"""

from names.models import LastName
import csv

MALE_FILENAME = '/home/szymon/dev/personal_data_generator/data_generation/names/NAZWISKA_MĘSKIE.csv'
FEMALE_FILENAME = '/home/szymon/dev/personal_data_generator/data_generation/names/NAZWISKA_ŻEŃSKIE.csv'

def run():
    to_database(MALE_FILENAME, True)
    to_database(FEMALE_FILENAME, False)


def to_database(filename, is_males):
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            
            next(reader) # skip the header

            for row in reader:
                if not row[0].startswith('BRAK DANYCH'):
                    # for female names, if the name already exists it means that it was added from male names
                    # this means that the name is gender - neutral and fits males and females
                    existing_obj = LastName.objects.filter(name=row[0]).first()

                    if existing_obj:
                        
                    
                    print(row[0])

                    new_name = LastName(name=row[0])
                    new_name.save()

        print('Finished importing from csv file to database')

    except FileNotFoundError:
        print(f'Failed to import data. File {filename} does not exist.')