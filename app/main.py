class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])
    for index, one in enumerate(people):
        if "wife" in one and one["wife"] is not None:
            Person.people[one["name"]].wife = Person.people[one["wife"]]
        if "husband" in one and one["husband"] is not None:
            Person.people[one["name"]].husband = Person.people[one["husband"]]
    return [Person.people[one["name"]] for one in people]


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]
