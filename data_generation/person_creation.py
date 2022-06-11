import random
from enum import Enum

from addresses.models import PostAddress, Street
from names.models import FirstName, LastName

from non_database import number_generator

ALL_TRUE_DICT = {
    "gen_first_name": True,
    "gen_last_name": True,
    "gen_phone": True,
    "gen_birth": True,
    "gen_pesel": True,
    "gen_street": True,
    "gen_house_number": True,
    "gen_post_code": True,
    "gen_city": True,
    "gen_county": True,
    "gen_voivodeship": True,
}

def random_first_name(male: bool) -> str:
    """Get one random first name from the database"""

    # get a list of all ids filtered by gender
    first_name_ids = FirstName.objects.filter(is_male=male).values_list(
        "id", flat=True
    )

    # pick a random id from the list and get the object with this id
    first_name_obj = FirstName.objects.get(id=random.choice(first_name_ids))

    # return just the string
    return first_name_obj.name.title()


def random_last_name(male: bool) -> str:
    """Get one random last name from the database"""

    # both genders can take neutral last names, pick a letter to exclude
    boolean_to_excluded_gender = {True: "F", False: "M"}

    # get the list of all ids, exluding the ones from opposite gender, but leaving neutral names
    last_name_ids = LastName.objects.exclude(
        matching_gender=boolean_to_excluded_gender[male]
    ).values_list("id", flat=True)

    # pick a random id from the list and get the object with this id
    last_name_obj = LastName.objects.get(id=random.choice(last_name_ids))

    # return just the string
    return last_name_obj.name


def random_street_name() -> str:
    """Get one random street from the database"""

    # get the list of all ids and pick a random one
    street_ids = Street.objects.values_list("id", flat=True)
    street_obj = Street.objects.get(id=random.choice(street_ids))

    # return just the string
    return street_obj.name


def generate_person_dict(
    requested_gender: str = "both",
    requested_values: dict = {},
    all_values_requested: bool = False,
    min_age: int = 18,
    max_age: int = 100,
):
    """
    Function to generate one person based on requested attributes and return a dictionary with all the data
    It uses both data from the database, and functions which generate random data on request
    """

    # if all values were requested, create a dict with all True values
    if all_values_requested:
        requested_values = ALL_TRUE_DICT

    # create an empty dict, fill it with only requested values
    # if the values are not requested, there is no need to randomize them / get them from database
    person_dict = {}

    # convert text gender to boolean (True if male, False if female)
    # if user picked both genders, randomize it
    gender_to_boolean = {
        "both": random.choice([True, False]),
        "female": False,
        "male": True,
    }

    male_requested = gender_to_boolean[requested_gender]

    # CHECK VALUES AND GENERATE THEM ONLY IF NEEDED
    if requested_values["gen_first_name"]:
        person_dict["first_name"] = random_first_name(male_requested)

    if requested_values["gen_last_name"]:
        person_dict["last_name"] = random_last_name(male_requested)

    if requested_values["gen_phone"]:
        person_dict["phone_number"] = number_generator.generate_phone_number()

    if requested_values["gen_pesel"] or requested_values["gen_birth"]:
        pesel_gen = number_generator.PeselGenerator(male_requested, min_age, max_age)

        if requested_values["gen_birth"]:
            person_dict["birth_date"] = pesel_gen.get_formatted_birth_date()

        if requested_values["gen_pesel"]:
            person_dict["pesel"] = pesel_gen.pesel

    # ADDRESS
    if requested_values["gen_street"]:
        person_dict["street_name"] = random_street_name()

    if requested_values["gen_house_number"]:
        person_dict["house_number"] = number_generator.generate_house_number()

    postaddr_attributes = ["post_code", "city", "county", "voivodeship"]

    # check if we need to get PostAddress from the database
    postaddress_requested = False

    for attr in postaddr_attributes:
        if requested_values[f"gen_{attr}"]:
            postaddress_requested = True
            break

    if postaddress_requested:
        post_ids = PostAddress.objects.values_list("id", flat=True)
        postaddr_obj = PostAddress.objects.get(id=random.choice(post_ids))

        for attr in postaddr_attributes:
            if requested_values[f"gen_{attr}"]:
                person_dict[attr] = getattr(postaddr_obj, attr)

    return person_dict
