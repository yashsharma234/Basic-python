
# a=int(input("enter the value of a"))
# b=int(input("enter the value of b"))
# print(a+b)
# a={12,23,35,43,67,76,4}
# print(a,type(a))
# n=int(input("enter the value of n:"))
# for i in range(1,11):
#     print(f"{n}*{i}={n*i}")
# n=int(input("enter the number:"))
# i=1
# sum=0
# while(i<=n):
#     sum+=i
#     i+=1
# # print(sum)
# n=int(input("enter the value of n:"))
# product=1
# for i in range(1,n+1):
#     product=product*i
# print(product)
# Library Management System using Basic Python and OOP Concepts


class Library:
class Student:
    def request_book(self):
        return input("Enter the name of the book you want to borrow: ")
    def return_book(self):
        return input("Enter the name of the book you want to return: ")
# Main Program Execution
if __name__ == "__main__":
    library = Library(["Python Basics", "OOP Concepts", "Data Structures"])
    student = Student()
    while True:
        print("\n====== Library Menu ======")
        print("1. Display Books")
        print("2. Lend Book")
        print("3. Add Book")
        print("4. Return Book")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if choice == 1:
            library.display_books()
        elif choice == 2:
            book = student.request_book()
            user = input("Enter your name: ")
            library.lend_book(book, user)
        elif choice == 3:
            book = input("Enter the name of the book to add: ")
            library.add_book(book)
        elif choice == 4:
            book = student.return_book()
            library.return_book(book)
        elif choice == 5:
            print("Thanks for using the Library Management System!")
   break
        else:
     print("Invalid choice. Please try again.")





class Student:
    def request_book(self):
        return input("Enter the name of the book you want to borrow: ")

    def return_book(self):
        return input("Enter the name of the book you want to return: ")

# Main Program Execution
if __name__ == "__main__":
    library = Library(["Python Basics", "OOP Concepts", "Data Structures"])
    student = Student()

    while True:
        print("\n====== Library Menu ======")
        print("1. Display Books")
        print("2. Lend Book")
        print("3. Add Book")
        print("4. Return Book")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            library.display_books()
        elif choice == 2:
            book = student.request_book()
            user = input("Enter your name: ")
            library.lend_book(book, user)
        elif choice == 3:
            book = input("Enter the name of the book to add: ")
            library.add_book(book)
        elif choice == 4:
            book = student.return_book()
            library.return_book(book)
        elif choice == 5:
            print("Thanks for using the Library Management System!")
            break
        else:
            print("Invalid choice. Please try again.")
