"""

https://www.matvaretabellen.no/api/
"""

import logging
import json
from pathlib import Path
import requests

logging.basicConfig(format="%(asctime)s %(levelname)s %(name)s %(message)s")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def save_to_json(thing: dict, location: str, folder: str, file_name: str):
    """Saves a dict as a json file

    thing: Thing to save as json file.
    location: Path to data folder.
    folder: Folder in data folder to store data in.
    file_name: Name for the json file.
    """
    if location.endswith("/"):
        raise ValueError("location can not end with '/'.")
    if folder.endswith("/"):
        raise ValueError("folder can not end with '/'.")
    if not file_name.endswith(".json"):
        raise ValueError("file_name must end with '.json'")
    directory = Path(location) / folder
    if not directory.exists():
        directory.mkdir(parents=True)
    with open(f"{location}/{folder}/{file_name}", "w", encoding="utf-8") as file:
        json.dump(thing, file, ensure_ascii=False, indent=4)


def get_foods():
    url = "https://www.matvaretabellen.no/api/nb/foods.json"
    response = send_request(url)
    for food_item in response.json()["foods"]:
        food_name = food_item["uri"].split("/")[-2]
        save_to_json(
            thing=food_item,
            location="data",
            folder="food",
            file_name=f"{food_name}.json",
        )


def get_food_groups(): ...


def get_nutrients(): ...


def get_langual(): ...


def get_sources(): ...


def send_request(url):
    logger.debug(f"Sending request to url: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        logger.debug("Success!")
        return response
    else:
        logger.warning(f"Response from {url}: {response.status_code}")


if __name__ == "__main__":
    get_foods()
