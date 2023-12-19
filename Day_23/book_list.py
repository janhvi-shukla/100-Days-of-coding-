books_list = [["Java", "$128"], ["C++", "$99"], ["Python", "$169"]]
ch = None
while ch != "3":
    print("\n1. Show Books List")
    print("2. Add a Book")
    print("3. Exit")
    print("Enter Your Choice (1-3): ", end="")
    ch = input()
    if ch == "1":
        print("\nBook\t\t Price")
        for book in books_list:
            book_name, book_price = book
            print(book_name, "\t\t", book_price)
    elif ch == "2":
        print("\nEnter the Name of Book: ", end="")
        book_name = input()
        print("Enter the Price: ", end="")
        book_price = input()
        book_price = "$" + book_price
        add_book = book_name, book_price
        books_list.append(add_book)
    elif ch == "3":
        print("\nOk!")
        break
    else:
        print("\nInvalid Choice!")
