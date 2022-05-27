class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, new_name):
        self.name = new_name
        print(f"Your new name is {self.name}")

    def change_age(self, new_age):
        self.age = new_age
        print(f"Hello {self.name}, Your new age is {self.age}")
    
    def add_track(self, new_track):
        self.tracks.append(new_track)
        print(f"Hello {self.name}, You've successfully added {new_track} to your tracks")
        print("Your new tracks are:")
        for i, track in enumerate(self.tracks):
            print(f"{i+1}. {track}")

    def get_score(self):
        print(f"Hello {self.name}, Your score is: {self.score}")


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
