import pandas as pd 


class CentralLibrary:

    def __init__(self,booklist):
        self.books = booklist

    def showBookNames(self):
        print("****All availabe books in the Library are****: \n\n")
        for item in self.books:
            print(item)

    def requestBook(self,bookname):

        if bookname in self.books:
            print(f"\nYou have been issued {bookname}. Please keep it safe and return it within 30 days and please handle it with care.\n")
            self.books.remove(bookname)
            return True

        else:
            print("\nSorry, This book is either not available or has already been issued to someone else. Please wait until the book is available\n")
            return False

    def returnbook(self,bookname):
        print(f"\nThanks for returning this book {bookname} Hope you enjoyed reading it. Have a great day ahead!\n")
        self.books.append(bookname)
        return True

class Student:

    def __init__(self):
        self.stbook =[]
    def requestBook(self):
       
        bookname =input("\nEnter the name of the book you want to borrow : \n")
        if (Library1.requestBook(bookname)):
           self.stbook.append(bookname)


    def returnBook(self):
        print("\nYou have taken the following books from the Library : \n")
        for index,item in enumerate(self.stbook):
            print(index+1,".",item )
        bookname =input("\nEnter the name of the book you want to return:\n ")
        Library1.returnbook(bookname)
        
        return bookname


bl1 = pd.read_csv("books.csv")
booklist1 = list(bl1["Title"])
Library1 = CentralLibrary(booklist1)
student1 = Student()

while(1):

    welcome = '''\n     ======== ======== ======== Welcome to Central Library ======== ======== ========
           \n                                Please choose an option:
                                1. List all the books
                                2. Request a book
                                3. Add/Return a book
                                4. Exit the Library

    '''
    print(welcome)
    a = int(input("Enter a Choice: "))
    print("\n")

    if a == 1:
        Library1.showBookNames()
    elif a ==2:
        student1.requestBook()
    elif a ==3:
        student1.returnBook()
    elif a ==4:
        print("Thanks for choosing Central Library. Have a great day ahead!")
        exit()
    else:
        print("Invalid Entry")


