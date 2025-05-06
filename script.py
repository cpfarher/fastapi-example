from typing import List, Tuple, Set, Union, Dict
import os

name = os.getenv("NAME", "Christian Pfarher")
print(f"Hello {name} from Python")

def get_full_name(first_name: str, last_name: str):
    return f"{first_name} {last_name}"


def process_list(lists: List[Union[str, int]], tuples: Tuple[int, int, str] = None, sets: Set[str] = None, dict: Dict[str, int] = None):
    for item in lists:
        if isinstance(item, str):
            print(item.capitalize())
        else:
            print(item)
    if tuples is not None:
        print("Tuples:")
        for item in tuples:
            print(item)
    if sets is not None:
        print("Sets:")
        for item in sets:
            print(item)
    if dict is not None:
        print("Dict:")
        for key, value in dict.items():
            print(f"{key}: {value}")

print(process_list([1,"a1", "2", "3"], sets={"a", "b", "c", "a"},tuples=(1, 2, 3), dict={"a": 1, "b": 2, "c": 3}))        
print(get_full_name("Christian", "Pfarher1")) # print when imported

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

# class Employee(Person):
#     def __init__(self, name: str, age: int, salary: int):
#         super().__init__(name, age)
#         self.salary = salary

#     def __str__(self):
#         return f"{self.name} is {self.age} years old and earns {self.salary} dollars"
    
if __name__ == "__main__":
    print(get_full_name("Christian", "Pfarher")) # print when run directly
