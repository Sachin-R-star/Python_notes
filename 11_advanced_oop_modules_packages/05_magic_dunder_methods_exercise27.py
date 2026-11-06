"""
================================================================================
LECTURE 110: Magic / Dunder Methods in Python (#lec106)
LECTURE 111: Coding Exercise #27 with Complete Solution (#lec107)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Magic / Dunder Methods kya hote hain?
   - "Dunder" = Double Underscore (`__method__`).
   - Python ke special built-in methods jo automatically trigger hote hain jab koi specific operation perform kiya jaye (e.g. `+`, `len()`, `str()`, `with`).

2. __str__ vs __repr__ (Top Interview Question):
   - `__str__`: End-user ke liye readable, user-friendly output. `print(obj)` aur `str(obj)` ise call karte hain.
   - `__repr__`: Developers aur debugging ke liye unambiguous representation (Aisi string jise copy karke code me chalaya ja sake: `eval(repr(obj)) == obj`).

3. Other Essential Dunder Methods:
   - `__len__(self)`: `len(obj)` call hone par execute hota hai.
   - `__getitem__(self, key)`: Indexing ya key access (`obj[0]` ya `obj['key']`) allow karta hai.
   - `__call__(self, ...)`: Object ko function ki tarah call karne allow karta hai (`obj()`).
   - `__del__(self)`: Destructor - jab object garbage collect/delete hota hai.
   - `__enter__` & `__exit__`: Custom Context Manager (`with` block) banane ke liye.

4. Exercise #27 - Book & Library Management System:
   - Custom Book class jisme title, author, aur pages hon.
   - Dunder methods: `__str__`, `__len__`, `__del__`, `__eq__`.
"""

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        print(f"[Constructor] Book '{self.title}' created.")

    # 1. __str__: User-friendly display
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # 2. __repr__: Formal representation for developers
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

    # 3. __len__: Returns number of pages
    def __len__(self):
        return self.pages

    # 4. __eq__: Check if two books are identical
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    # 5. __call__: Invoking book object like a function
    def __call__(self, reader_name):
        print(f"{reader_name} is currently reading '{self.title}'!")

    # 6. __del__: Destructor
    def __del__(self):
        print(f"[Destructor] Book '{self.title}' destroyed from memory.")


# --- Custom Collection using __getitem__ ---
class Bookshelf:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def __len__(self):
        return len(self._books)

    def __getitem__(self, index):
        """Enables indexing: shelf[0] and slicing shelf[1:3]"""
        return self._books[index]


# --- Verification Code ---
if __name__ == "__main__":
    print("==========================================")
    print("   TESTING DUNDER METHODS & EXERCISE 27   ")
    print("==========================================")

    b1 = Book("Fluent Python", "Luciano Ramalho", 790)
    b2 = Book("Fluent Python", "Luciano Ramalho", 790)
    b3 = Book("Python Crash Course", "Eric Matthes", 544)

    # Testing __str__ and __repr__:
    print("\n__str__ output  :", str(b1))
    print("__repr__ output :", repr(b1))

    # Testing __len__:
    print("len(b1) (pages) :", len(b1))

    # Testing __eq__:
    print("Is b1 == b2?    :", b1 == b2)  # True
    print("Is b1 == b3?    :", b1 == b3)  # False

    # Testing __call__:
    b1("Sachin")

    # Testing Bookshelf custom collection (__len__ and __getitem__):
    shelf = Bookshelf()
    shelf.add_book(b1)
    shelf.add_book(b3)
    print(f"\nBookshelf total books: {len(shelf)}")
    print(f"Book at index 0      : {shelf[0]}")
    print(f"Book at index 1      : {shelf[1]}")

    # Explicit deletion triggers __del__:
    print("\nDeleting b3 explicitly:")
    del b3
