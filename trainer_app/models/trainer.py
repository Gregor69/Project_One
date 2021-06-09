class Trainer:
    def __init__(self, first_name, last_name, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    # method will return full name of trainer from class
    # define full name
    # return first and last names from properties of trainer class

    def full_name(self):
        return f"{self.first_name} {self.last_name}"