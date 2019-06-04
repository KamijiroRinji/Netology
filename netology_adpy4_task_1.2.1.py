import json
import wikipedia


class GetWikiLink:
    def __init__(self, path):
        self.file = open(path, encoding="utf8")
        self.countries = json.load(self.file)

    def __iter__(self):
        return (f'{country}: {wikipedia.page(country).url}' for country in self.countries)


if __name__ == "__main__":
    countries = [country for country in GetWikiLink("countries.json")]
    with open("countries.json", "w") as file_write:
        json.dump(countries, file_write, ensure_ascii=False, indent=2)
