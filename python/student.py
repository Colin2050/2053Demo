class Student:
    def __init__(self,fname,lname,id,energy_level):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.energy_level = 10
    def __str__(self):
        return f"{self.lname}: {self.id}"
    def greeting(self):
        print(f"Hello, my name is {self.fname} {self.lname} and my id is {self.id}")
    def take_exam(self):
        self.energy_level -= 1
    def get_energy_level(self):
        return self.energy_level
    