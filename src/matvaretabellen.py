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

URL_BASE = "https://www.matvaretabellen.no/api"


def save_to_json(
    thing: dict, location: str, folder: str, file_name: str, language: str
):
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
    directory = Path(location) / language / folder
    if not directory.exists():
        directory.mkdir(parents=True)
    with open(
        f"{location}/{language}/{folder}/{file_name}", "w", encoding="utf-8"
    ) as file:
        json.dump(thing, file, ensure_ascii=False, indent=4)


def get_foods(language):
    url = f"{URL_BASE}/{language}/foods.json"
    response = send_request(url)
    for food_item in response.json()["foods"]:
        food_name = food_item["uri"].split("/")[-2]
        save_to_json(
            thing=food_item,
            location="data",
            folder="food",
            file_name=f"{food_name}.json",
            language=language,
        )


def get_food_groups(language):
    url = f"{URL_BASE}/{language}/food-groups.json"
    response = send_request(url)
    for food_group in response.json()["foodGroups"]:
        file_name = f"{food_group['name'].lower()}.json"
        save_to_json(
            thing=food_group,
            location="data",
            folder="food_group",
            file_name=file_name,
            language=language,
        )


def get_nutrients(language):
    url = f"{URL_BASE}/{language}/nutrients.json"
    response = send_request(url)
    for nutrient in response.json()["nutrients"]:
        file_name = f"{nutrient['name'].lower()}.json"
        save_to_json(
            thing=nutrient,
            location="data",
            folder="nutrients",
            file_name=file_name,
            language=language,
        )


def get_langual(language):
    url = f"{URL_BASE}/langual.json"
    response = send_request(url)
    save_to_json(
        thing=response.json()["codes"],
        location="data",
        folder="langual",
        file_name="langual.json",
        language=language,
    )


def get_sources(language):
    url = f"{URL_BASE}/{language}/sources.json"
    response = send_request(url)
    for source in response.json()["sources"]:
        file_name = f"{source['sourceId']}.json"
        save_to_json(
            thing=source,
            location="data",
            folder="sources",
            file_name=file_name,
            language=language,
        )


def send_request(url):
    logger.debug(f"Sending request to url: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        logger.debug("Success!")
        return response
    else:
        logger.warning(f"Response from {url}: {response.status_code}")


def main():
    languages = ["nb", "en"]
    for language in languages:
        get_foods(language)
        get_food_groups(language)
        get_nutrients(language)
        get_langual(language)
        get_sources(language)


if __name__ == "__main__":
    main()
