# Colin Duncan
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_checked_out = False
    def __str__(self):
        return f"{self.title} by {self.author}: {self.is_checked_out}"
    def check_out(self):
        if self.is_checked_out == False:
            self.is_checked_out = True
        else:
            print( "This book is already checked out")
    def return_book(self):
        if self.is_checked_out == True:
            self.is_checked_out = False
        else:
           print("This book is already returned")
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_genre(self):
        return self.genre
    def checked_out(self):
        return self.is_checked_out