"""Script to get a photo from thispersondoesnotexist.com and download it"""

import requests

PHOTO_URL = "https://thispersondoesnotexist.com/image"
PHOTO_PATH = "static/images/generated_person.jpg"


def save_generated_photo():
    # download the photo to specified local path
    # we download the photo so that there will always be something to be displayed,
    # even if thispersondoesnotexist is not working

    response = requests.get(PHOTO_URL)
    print(response.status_code)
    if response.status_code == 200:
        with open(PHOTO_PATH, "wb") as file:
            file.write(response.content)


if __name__ == "__main__":
    # only for testing purposes
    save_generated_photo()
