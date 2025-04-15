# Colin Duncan
import book
books = []
i = 0
with open("books.txt") as file:
    for line in file:
        info = line.split(",")
        books.append(book.Book(info[0],info[1],info[2]))
        print(books[i])
        i+=1
print(books[0].get_title()) # Output: To Kill a Mockingbird
print(books[0].get_author()) # Output: Harper Lee
print(books[0].get_genre()) # Output: Fiction
print(books[0].checked_out()) # Output: False
books[0].check_out()
print(books[0])
books[0].return_book()
print(books[0])

        