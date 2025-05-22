class Library1:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self):
        no_book = int(input("How many books you want to add: "))
        for i in range(no_book):
            book = input("Enter Book Name: ")
            self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The Library has {self.noBooks} Books.")

l1 = Library1()
l1.addBook()
l1.showInfo()
