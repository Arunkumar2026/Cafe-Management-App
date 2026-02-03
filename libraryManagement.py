'''
this is  a library management program in this program we can register the user,
add books to the library, view users, view books, borrow books from other users, 
and return the books to that user.
'''

import os # importing os module
import json # importing json module

USER_FILE = 'libraryUsers.json' # importing library users in the USER_FILE variable
BOOK_FILE = 'libraryBooks.json' # importing library books in the BOOK_FILE variable

#this function is to load the data in json file
def load_json(file_name):
    if not os.path.exists(file_name): # checking if the file is present or not, if the file is not present then the condition will be true.
        return [] # if the file is not present then we are returning the empty list
    try: # if the file is present then we are trying different methods
        with open(file_name,'r') as f: # opening the file and reading the file with 'r' method and saving the file with alias name f
           return json.load(f)
    # to handle the errors we have to use excepts
    except json.JSONDecodeError:
        return []

#this function will save the data in the user file
def save_json(file_name,data):
    with open(file_name, 'w') as f: #opening the file in wrirte mode 'w'
        #this dump function will save the user data in the user file 
        #data is the user data, f is the file mode, indent is the staring spaces
        json.dump(data,f,indent=4) 


#this function will register the new user 
def register_user(users):
    name = input("Enter your name: ").strip()

    #we have to check weather the user is already exist in the user date if the user is already exist then we should not register again.
    #to check this we have to use the conditon operator
    if any(u['name'] == name for u in users): # this is the generator expression with any() method  
        print("User already registered.\n")
        return users
    #if the user is not existed in the data then we have to register the new user
    user = {'name':name, 'borrowed_books': []}
    users.append(user)

    #we have to save this data in the user file 
    save_json(USER_FILE,users) #this function will save the data in the user file

    #showing the success message to the user 
    print(f'user: {name} registered successfully.\n')
    return users


#this is the main function
def main():
    users = load_json(USER_FILE) # calling the load_json function and the returned data is stored in users variable 
    books = load_json(BOOK_FILE) # calling the load_json function and the returned data is stored in books variable

    # creating a inifinity while loop
    while True:
        # this are the menu options shown to the user
        print("===== LibrarySys Menu =====")
        print("1. Register User")
        print("2. View Users")
        print("3. Add Book")
        print("4. View Books")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")

        #taking the user input of the given options and storing it in the choice variable
        choice = input("Choose an option: ")

        #checking the option selected by the user with the conditions
        #if any option is matched with any condition then the assigned function will be called.
        if choice == "1":
            users = register_user(users)
        elif choice == "2":
            view_users(users)
        elif choice == "3":
            add_book(books)
        elif choice == "4":
            view_books(books)
        elif choice == "5":
            borrow_book(books, users)
        elif choice == "6":
            return_book(books, users)
        elif choice == "7":
            print("Existing LibrarySys... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n") 


main()