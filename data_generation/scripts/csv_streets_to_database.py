"""Script to add many street names from csv file"""

from addresses.models import Street
import csv

CSV_FILENAME = '/home/szymon/dev/personal_data_generator/data_generation/addresses/street_names.csv'

def run():
    try:
        with open(CSV_FILENAME) as file:
            reader = csv.reader(file, delimiter=';')
            
            next(reader) # skip the header

            # clean the existing data in the database
            Street.objects.all().delete()

            for row in reader:
                if row[1]: 
                    # space is added between segments, for example Adama Mickiewicza
                    result_name = f'{row[1]} {row[0]}'
                else:
                    # no need to add space
                    result_name = row[0]

                print(result_name)

                new_address = Street(name=result_name)
                new_address.save()

        print('Finished importing from csv file to database')

    except FileNotFoundError:
        print(f'Failed to import data. File {CSV_FILENAME} does not exist.')