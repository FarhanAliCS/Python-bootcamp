from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str


person=Person("Ali",24,"Peshawer")
print(person)