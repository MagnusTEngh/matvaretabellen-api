"""
https://github.com/TandoorRecipes/open-tandoor-data/tree/main
"""
import glob

class TandoorFoodData:
    def __init__(self, language):

        self.language = language
        self.from_matvaretabellen()

    def from_matvaretabellen(self):
        path = f"data/{self.language}/food/*.json"
        print(path)
        for food in glob.glob(path):
            print(food)


class TandoorFood:

    def __init__(self, language):
        self.language = language

    def get_from_foods(self):
        ...

    def get_from_




if __name__ == "__main__":
    TandoorFoodData("nb")
