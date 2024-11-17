# Challenge 12
library = {}

def add_book(library, book, author):
    if author in library:
        library[author].append(book)
    else:
        library[author] = [book]

# Define a book

book = {
    'title': 'Animal Farm',
    'year_published': '1945',
    'genre': 'Dystopian'
}

add_book(library, book, 'George Orwell')
# Nevermind actually quite useful storing a lot of info on a certain group of variables by name
print(library)