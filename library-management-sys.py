
class Book:
    def __init__(self, id, name, category, quantity):
        self.id = id
        self.name = name 
        self.category = category
        self.quantity = quantity

class User:
    def __init__(self, username, name, password):
        self.username = username
        self.name = name
        self.password = password
        self.borrowed = []
        self.returns = []

class Library:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.books = []
        self.users = []

    def add_book(self, id, name, cat, quan):
        book = Book(id, name, cat, quan)
        self.books.append(book)
        print(f"\t'{name}' Added successfully!")
        return book
        
    def add_user(self, username, name, password):
        user = User(username, name, password)
        self.users.append(user)

        return user
    
    def borrow_book(self, user, book_id):
        for book in self.books:
            if book.id == book_id:
                if book in user.borrowed:
                    print("\n\tAlready borrowed!")
                    return
                elif book.quantity < 1:
                    print("\n\tNot available!")
                    return
                else:
                    user.borrowed.append(book)
                    book.quantity -= 1
                    print(f"\n\t'{book.name}' x1 borrowed successfully!")
                    return
        print("\n\tNot available in this library!")
    
    def return_book(self, user, book_id):
        for book in user.borrowed:
            if book.id == book_id:
                for b in self.books:
                    if b.id == book_id:
                        b.quantity += 1
                        user.borrowed.remove(book)
                        user.returns.append(book)
                        print(f"\n\t'{book.name}' Returned!")
                        return
        print("\n\tBook not found with id:", book_id)

    def my_books(self, user):
        print("\n\tID\tName\tCategory")
        print("\t--\t----\t--------")
        for book in user.borrowed:
            print(f"\t{book.id}\t{book.name}\t{book.category}")

    def my_returns(self, user):
        print("\n\tID\tName\tTime")
        print("\t--\t----\t----")
        for book in user.returns:
            print(f"\t{book.id}\t{book.name}\t{book.category}")

    

aal = Library("AlgoAspire-Library", "Shakib")
admin = aal.add_user("admin", "admin", "1234")
curr_user = admin
is_admin = True

while True:
    if curr_user == None:
        print("\n\tNot logged in!")
        option = input("\n\tRegister/Login (R/L): ")

        if option == "R":
            name = input("\tEnter your Name: ")
            username = input("\tEnter your username: ")
            password = input("\tEnter your password: ")

            if username in aal.users:
                print(f"Username: {username} is unavailable!")
                continue

            user = aal.add_user(username, name, password)
            curr_user = user
            is_admin = False
            print("\n\tRegistration successful!")

        elif option == "L":
            username = input("\tEnter username: ")
            password = input("\tEnter your password: ")
            
            match = False
            for user in aal.users:
                if user.username == username and user.password == password:
                    if username == admin.username and password == admin.password:
                        curr_user = user
                        match = True
                        is_admin = True
                        print("\n\tAdmin login successful!")

                    else:
                        curr_user = user
                        match = True
                        is_admin = False
                        print("\n\tLogin successful!")
                    break
            
            if not match:
                print("Invalid Username or Password!")

    else:
        if is_admin:
            print("\nAdmin Panel:")
            print("1. Add Book")
            print("2. Show Users")
            print("3. Available Books")
            print("4. Logout")
            print("5. Exit")

            op = input(">>> ")
            if op == "1":
                id = int(input("\tBook id: "))
                name = input("\tBook name: ")
                cat = input("\tEnter Category: ")
                quan = int(input("\tEnter Quantity: "))

                aal.add_book(id, name, cat, quan)

            elif op == "2":
                print("\tName\tUsername")
                print("\t----\t--------")
                for user in aal.users:
                    print(f"\t{user.name}\t{user.username}")
                print()

            elif op == "3":
                print("\n\tID\tName\tCategory\tCopies")
                print("\t--\t----\t--------\t------")
                for book in aal.books:
                    print(f"\t{book.id}\t{book.name}\t{book.category}\t{book.quantity}")

            elif op == "4":
                curr_user = None
                continue

            elif op == "5":
                exit()

            else:
                print("\n\tPlease enter valid input!")
                
        else:
            print("\nUser menu:")
            print("1. Borrow a Book")
            print("2. Return a Book")
            print("3. My Books")
            print("4. My Returns")
            print("5. Available Books")
            print("6. Logout")
            print("7. Exit")

            op = input(">>> ")
            if op == "1":
                book_id = int(input("\n\tEnter book id: "))
                aal.borrow_book(curr_user, book_id)
            
            elif op == "2":
                book_id = int(input("\n\tEnter book id: "))
                aal.return_book(curr_user, book_id)

            elif op == "3":
                aal.my_books(curr_user)

            elif op == "4":
                aal.my_returns(curr_user)
            
            elif op == "5":
                print("\n\tID\tName\tCategory\tCopies")
                print("\t--\t----\t--------\t------")
                for book in aal.books:
                    print(f"\t{book.id}\t{book.name}\t{book.category}\t{book.quantity}")

            elif op == "6":
                curr_user = None
                continue
            
            elif op == "7":
                exit()

            else:
                print("\n\tInvalid command!")
