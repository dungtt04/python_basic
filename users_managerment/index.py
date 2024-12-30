import sqlite3
from app.controllers import UserController
from app.models import init_db

def main():
    controller = UserController()

    # Initialize the database
    init_db()

    while True:
        print("\nMenu:")
        print("1. Create a user")
        print("2. List all users")
        print("3. Update a user")
        print("4. Delete a user")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            try:
                controller.add_user(name, email, password)
            except ValueError as e:
                print(e)
        elif choice == '2':
            controller.list_users()
        elif choice == '3':
            user_id = int(input("Enter user ID to update: "))
            new_name = input("Enter new name: ")
            new_email = input("Enter new email: ")
            new_password = input("Enter new password: ")
            try:
                controller.edit_user(user_id, new_name, new_email, new_password)
            except ValueError as e:
                print(e)
        elif choice == '4':
            user_id_to_delete = int(input("Enter user ID to delete: "))
            controller.remove_user(user_id_to_delete)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
