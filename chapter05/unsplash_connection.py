import json
import os
import random
import shutil
from typing import Tuple

import requests
from dotenv import load_dotenv

load_dotenv(".env")

verbose = True

access_key = os.getenv("unsplash_access_key")
api = os.getenv("unsplash_api")

headers = {
    "Authorization": f"Client-ID {access_key}"
}


def get_picture_by_keywords(keywords: str, image_filepath: str) -> Tuple[bool, str]:
    response = requests.get(f"{api}/search/photos?query={keywords}",
                            headers=headers)

    if response.status_code != 200:
        print(f"Unsplash: {response.text}")
        return False, ""

    response = json.loads(response.text)

    picture_data = random.choice(response["results"])

    # Download picture
    response = requests.get(picture_data["urls"]["regular"], stream=True)
    response.raw.decode_content = True
    with open(image_filepath, 'wb') as f:
        shutil.copyfileobj(response.raw, f)

    return True, picture_data


def get_first_pages(keywords: str, page: int) -> list:
    all_results = []
    for i in range(1, page + 1):
        response = requests.get(f"{api}/search/photos?query={keywords}&page={i}",
                                headers=headers)

        if response.status_code != 200:
            print(f"Unsplash: {response.text}")
            break

        all_results += json.loads(response.text)['results']

    return all_results


if __name__ == '__main__':
    keywords = "cats"
    print(get_picture_by_keywords(keywords, "tmp.jpg"))
