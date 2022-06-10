import random
from enum import Enum

from addresses.models import PostAddress, Street
from names.models import FirstName, LastName

from non_database import number_generator


class GenderLetter(Enum):
    MALE = "M"
    FEMALE = "F"
    NEUTRAL = "N"


def generate_person_dict(
    requested_gender: str = "both",
    requested_values: dict = {},
    all_values_requested: bool = False,
):
    """Function to generate one person and return a dictionary with all the data"""
    assert requested_gender in ("both", "female", "male")

    # if all values were requested, create a dict with all True values
    if all_values_requested:
        requested_values = {
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

    if requested_values["gen_pesel"] or requested_values["gen_birth"]:
        pesel_gen = number_generator.PeselGenerator(male_requested)

    # CHECK VALUES AND GENERATE THEM ONLY IF NEEDED
    if requested_values["gen_first_name"]:
        first_name_ids = FirstName.objects.filter(is_male=male_requested).values_list(
            "id", flat=True
        )
        first_name_obj = FirstName.objects.get(id=random.choice(first_name_ids))
        person_dict["first_name"] = first_name_obj.name.title()

    if requested_values["gen_last_name"]:
        # both genders can take neutral last names, pick a letter to exclude
        boolean_to_excluded_gender = {True: GenderLetter.FEMALE, False: GenderLetter.MALE}

        last_name_ids = LastName.objects.exclude(
            matching_gender=boolean_to_excluded_gender[male_requested]
        ).values_list("id", flat=True)
        last_name_obj = LastName.objects.get(id=random.choice(last_name_ids))
        person_dict["last_name"] = last_name_obj.name

    if requested_values["gen_phone"]:
        person_dict["phone_number"] = number_generator.generate_phone_number()

    if requested_values["gen_birth"]:
        person_dict["birth_date"] = pesel_gen.get_formatted_birth_date()

    if requested_values["gen_pesel"]:
        person_dict["pesel"] = pesel_gen.pesel

    # ADDRESS
    post_ids = PostAddress.objects.values_list("id", flat=True)
    postaddr_obj = PostAddress.objects.get(id=random.choice(post_ids))

    street_ids = Street.objects.values_list("id", flat=True)
    street_obj = Street.objects.get(id=random.choice(street_ids))

    if requested_values["gen_street"]:
        person_dict["street_name"] = street_obj.name

    if requested_values["gen_house_number"]:
        person_dict["house_number"] = number_generator.generate_house_number()

    if requested_values["gen_post_code"]:
        person_dict["post_code"] = postaddr_obj.post_code

    if requested_values["gen_city"]:
        person_dict["city"] = postaddr_obj.city

    if requested_values["gen_county"]:
        person_dict["county"] = postaddr_obj.county

    if requested_values["gen_voivodeship"]:
        person_dict["voivodeship"] = postaddr_obj.voivodeship

    return person_dict