# This is Python Chatting Program

users = []
chat_histroy = []



def show_menu():
    print("\n---PyChat Menu---")
    print("1.Register User")
    print("2.Send Message")
    print("3.Show Chat History")
    print("4.Exit")

def register_user():
    global users 
    name = input("Enter you user name: ")
    if name in users:
        print("Username already exitsted")
    else:
        users.append(name)
        print(f'{name} registered successfully.')

def send_message():
    global users, chat_histroy
    sender = input("Enter your username: ")
    if sender not in users:
        print("User not registered")
        return 
    receiver = input("Enter receiver username: ")
    if receiver not in users:
        print("Receiver not registered")
        return 
    
    message = input("Enter you message: ")

    chat = f'{sender} -> {receiver}: {message}'

    chat_histroy.append(chat)
    print("Message sent")


def show_chat_history():
    global chat_histroy
    print("-----Chat History-----")
    if chat_histroy:
        for msg in chat_histroy:
            print(msg)
    else:
        print("No Messages Yet")
        


def menu():
    while True:
        show_menu()

        choice = input("Enter your Choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            send_message()
        elif choice == "3":
            show_chat_history()
        elif choice == "4":
            print("Exiting PyChat, Goodbye")
            break 
        else:
            print("Invalid choice. Try again.")

menu()