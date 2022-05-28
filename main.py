import traceback
from unicodedata import name

class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track, score):
        self.name = str(name)
        self.age = int(age)
        self.track = list(track)
        self.score = float(score)
    

    def change_name(self, new_name):
        self.new_name = new_name
        new_name =input("What is your name?:")
        print("The student new name is:" self.new_name)

    def change_age(self, new_age):
        self.change_age = new_age
        new_age =input("What is your age now?:")
        print("The student new age is:" self.new_age)

    def add_track(self, new_track):
        self.add_track = new_track
        print("The student track is:" self.new_track)

    def get_score(self, new_score):
        self.get_score = new_score
        print("The student score is:" self.new_score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
