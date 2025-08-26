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


def get_food_groups():
    url = "https://www.matvaretabellen.no/api/nb/food-groups.json"
    response = send_request(url)
    for food_group in response.json()["foodGroups"]:
        file_name = f"{food_group['name'].lower()}.json"
        save_to_json(
            thing=food_group,
            location="data",
            folder="food_group",
            file_name=file_name,
        )


def get_nutrients():
    url = "https://www.matvaretabellen.no/api/nb/nutrients.json"
    response = send_request(url)
    for nutrient in response.json()["nutrients"]:
        file_name = f"{nutrient['name'].lower()}.json"
        save_to_json(
            thing=nutrient,
            location="data",
            folder="nutrients",
            file_name=file_name,
        )


def get_langual():
    url = "https://www.matvaretabellen.no/api/langual.json"
    response = send_request(url)
    save_to_json(
        thing=response.json()["codes"],
        location="data",
        folder="langual",
        file_name="langual.json",
    )


def get_sources():
    url = "https://www.matvaretabellen.no/api/nb/sources.json"
    response = send_request(url)
    for source in response.json()["sources"]:
        file_name = f"{source['sourceId']}.json"
        save_to_json(
            thing=source,
            location="data",
            folder="sources",
            file_name=file_name,
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
    get_foods()
    get_food_groups()
    get_nutrients()
    get_langual()
    get_sources()


if __name__ == "__main__":
    main()
