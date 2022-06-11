## Django app which generates personal data based on Polish addresses and Polish names.

**Generated data:**
 - Postcodes with city, county and voivodeship (42345 records in the database - all polish postcodes)
 - Street names (29310 records in the database)
 - First names (top 100 most popular for males and females as of 24.01.2022)
 - Last names (top 10000 most popular for males and females as of 24.01.2022)
 - Phone numbers
 - Birth dates
 - PESEL numbers based on birth dates

**Use cases:**
 - generating data to test your software
 - generating data to later import to other programs, like MS Access
 - getting a random names for different purposes if you are not creative

**Structure:**
 
├── addresses - Django app for address data

├── data_generation - Home of the django app

├── names - Django app for people names data

├── non_database - Directory for generating data on request

├── scripts - Scripts used to initially populate the database

├── static - Static files

├── templates - HTML templates

**Requirements to run**

All packages are specified in requirements.txt

> pip install -r requirements.txt