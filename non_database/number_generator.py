import random
import string
from datetime import date
from calendar import monthrange


class PeselGenerator:
    """A class that can generate birth date and pesel number, as birth date is strictly required for PESEL generation"""

    def __init__(self, is_male: bool, min_age: int, max_age: int) -> None:
        self.is_male = is_male
        self.min_age = min_age
        self.max_age = max_age
        self.generate_birth_date()
        self.pesel = self.generate_pesel()

    def generate_birth_date(self) -> None:
        """Generate a birth date in between requested min_age and max_age - in age we only consider years"""
        self.year = random.randint(
            date.today().year - self.max_age, date.today().year - self.min_age
        )
        self.month = random.randint(1, 12)

        # monthrange gives us the number of days in a month, takes leap years in consideration
        month_length = monthrange(self.year, self.month)[1]
        self.day = random.randint(1, month_length)

    def generate_pesel(self) -> str:
        """Generate PESEL number based on person's gender and birth date, using the real algorithm"""
        result = ""
        # following comments are in polish because I copied them from wikipedia page about PESEL, sorry

        if self.year < 2000:
            # dla osób urodzonych w latach 1900 do 1999 – miesiąc zapisywany jest w sposób naturalny,
            # tzn. dwucyfrowo od 01 do 12
            result += f"{str(self.year)[2:]}{self.month:02d}{self.day:02d}"

        else:
            # dla osób urodzonych w innych latach niż 1900–1999 dodawane są do numeru miesiąca wielkości
            result += f"{str(self.year)[2:]}{self.month + 20}{self.day:02d}"

        # series number
        result += str(random.randint(100, 999))

        # Informacja o płci osoby, której zestaw informacji jest identyfikowany,
        # zawarta jest na 10. (przedostatniej) pozycji numeru PESEL.

        gender_digits = {
            "male": [x for x in range(0, 10) if x % 2 == 1],
            "female": [x for x in range(0, 10) if x % 2 == 0],
        }

        if self.is_male:
            result += str(random.choice(gender_digits["male"]))
        else:
            result += str(random.choice(gender_digits["female"]))

        # last digit - control number

        # dla kolejnych dziesięciu cyfr identyfikatora PESEL obliczany jest iloczyn cyfry i jej wagi,
        # obliczana jest suma tych iloczynów
        WEIGHTS = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
        S_number = sum([int(digit) * WEIGHTS[int(digit)] for digit in result])

        M_number = S_number % 10

        if M_number == 0:
            result += str(M_number)
        else:
            result += str(10 - M_number)

        return result

    def get_formatted_birth_date(self) -> str:
        """Format birth date, example: 31.12.1999"""
        return f"{self.day}.{self.month}.{self.year}"


def generate_house_number():
    """Generate a string house or apartment number, either one number or with flat number after slash"""

    # base number is a positive integer smaller than 100
    result = str(random.randint(1, 99))

    if random.randint(1, 5) == 1:
        # add a letter - picking from 10 first letters of the alphabet
        result += random.choice(string.ascii_lowercase[:10])

    if random.randint(1, 2) == 1:
        # add an apartment number
        result += f" / {random.randint(1, 99)}"

    return result


def generate_phone_number():
    """Generate a string phone number"""
    return str(random.randint(500000000, 900000000))
