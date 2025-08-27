"""
https://github.com/TandoorRecipes/open-tandoor-data/tree/main
"""


import json

with open("/home/magnus/projects/matvaretabellen-api/data/nb/food/agurksalat.json", 'r') as file:
    data = json.load(file)

print(data.keys())

print(data["calories"])


class TandoorImportableFood:



    def __init__(self):
        self.name
        self.plural_name
        self.description
        self.url =
        self.properties = self.get_properties()
        self.properties_food_amount
        """ Needed????
        "properties_food_amount": 100.0,
        "properties_food_unit": {
            "id": 5,
            "name": "g",
            "plural_name": "g",
            "description": null,
            "base_unit": "g",
            "open_data_slug": "unit-g"
        },
        """
        self.supermarket_category = self.get_category()
        self.full_name
        self.open_data_slug
        self.unit_name
        self.unit_plural_name
        self.unit_base_unit
        self.unit_open_data_slug
        self.unit_amount
        self.conversions = self.get_conversions()


    def get_properties(self) -> list[TandoorFoodProperty]:
        properties = []
        for food_item in foods:
            properties.append(
                TandoorFoodProperty(

                ).to_dict()
            )

    def get_category(self):
        ...

    def get_conversions(self):
        ...
        conversions = []
        for conversion in :
            conversions.append(
                TandoorFoodConversion(

                ).to_dict()
            )



class TandoorFoodProperty:

    def __init__(self):
        self.property_amount
        self.property_type
        self.property_name
        self.property_unit
        self.open_data_slug

    def to_dict(self):
        ...

class TandoorFoodCategory:

    def __init__(self):
        self.id # Needed?
        self.name
        self.open_data_slug

    def to_dict(self):
        ...


class TandoorFoodConversion:

    def __init__(self):
        self.food
        self.unit
        self.amount

    def to_dict(self):
        ...
