from queries.for_running import if_not_used

from auth.login import login
from auth.register import register



def after_login(email: str, status: str):
    """
    Function to handle the after-login actions.
    """
    if status == "super":
        print("Welcome Super Admin!")

    elif status == "admin":
        print("Welcome Admin!")

    elif status == "user":
        print("Welcome User!")

    elif status == "courier":
        print("Welcome Courier!")

    elif status == "manager":
        print("Welcome Manager!")

    elif status == "employee":
        print("Welcome Employee!")

    elif status == "developer":
        print("Welcome Developer!")


def main():
    print("\n1. Login\n"
          "2. Register\n"
          "3. Exit\n")

    print("""
    super admin login&password = super
    """)
    choice = input("Enter your choice: ")

    if choice == '1':
        data = login()
        if not data:
            return main()
        email, status = data
        after_login(email, status)

    elif choice == '2':
        email = register()
        after_login(email, "user")

    elif choice == '3':
        print("Exiting...")
        return None

    else:
        print("Invalid choice. Please try again.")

    return main()


if __name__ == "__main__":
    if_not_used()
    main()