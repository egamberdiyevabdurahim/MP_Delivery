from queries.for_running import if_not_used

from auth.login import login

from user.super_admin.super_admin_menu import statistics_menu


def after_login(email: str, status: str):
    """
    Function to handle the after-login actions.
    """
    if status == "super":
        pass

    elif status == "admin":
        pass

    elif status == "user":
        pass

    elif status == "courier":
        pass

    elif status == "manager":
        pass

    elif status == "employee":
        pass

    elif status == "developer":
        pass


def main():
    print("\n1. Login\n"
          "2. Register\n"
          "3. Exit\n")

    print("""
    super admin login&password = super
    """)
    choice = input("Enter your choice: ")

    if choice == '1':
        email, status = login()
        after_login(email, status)

    elif choice == '2':
        pass

    elif choice == '3':
        print("Exiting...")
        return None

    else:
        print("Invalid choice. Please try again.")

    return main()


if __name__ == "__main__":
    if_not_used()
    main()