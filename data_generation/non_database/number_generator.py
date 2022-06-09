import random
import string
from datetime import date
from calendar import monthrange

MINIMAL_BIRTH_YEAR = 1930

class PeselGenerator:
    def __init__(self, is_male: bool) -> None:
        self.is_male = is_male
        self.generate_birth_date()
        self.pesel = self.generate_pesel()

    def generate_birth_date(self) -> None:
        self.year = random.randint(MINIMAL_BIRTH_YEAR, date.today().year - 18)
        self.month = random.randint(1, 12)
        
        # monthrange gives us the number of days in a month, takes leap years in consideration
        month_length = monthrange(self.year, self.month)[1]
        self.day = random.randint(1, month_length)

    def generate_pesel(self) -> str:
        """Generate PESEL number based on person's gender and birth date"""
        result = ''

        if self.year < 2000:
            # dla osób urodzonych w latach 1900 do 1999 – miesiąc zapisywany jest w sposób naturalny,
            # tzn. dwucyfrowo od 01 do 12
            result += f"{str(self.year)[2:]}{self.month:02d}{self.day}"
        else:
            # dla osób urodzonych w innych latach niż 1900–1999 dodawane są do numeru miesiąca wielkości
            result += f"{str(self.year)[2:]}{self.month + 20}{self.day}"

        # series number
        result += str(random.randint(100, 999))

        # Informacja o płci osoby, której zestaw informacji jest identyfikowany,
        # zawarta jest na 10. (przedostatniej) pozycji numeru PESEL. 
        
        gender_digits = {'male': [x for x in range(0, 10) if x % 2 == 1], 'female': [x for x in range(0, 10) if x % 2 == 0]}

        if self.is_male:
            result += str(random.choice(gender_digits['male']))
        else:
            result += str(random.choice(gender_digits['female']))

        result += str(random.randint(1, 10))

        return result


    def get_formatted_birth_date(self) -> str:
        return f'{self.day}.{self.month}.{self.year}'


def generate_house_number():
    """Generate a string house or apartment number"""
    
    # base number is a positive integer smaller than 100
    result = str(random.randint(1, 99))

    if random.randint(1, 5) == 1:
        # add a letter - picking from 10 first letters of the alphabet
        result += random.choice(string.ascii_lowercase[:10])

    if random.randint(1, 2) == 1:
        # add an apartment number
        result += f' / {random.randint(1, 99)}'

    return result


def generate_phone_number():
    """Generate a string phone number"""
    return str(random.randint(500000000, 900000000))

