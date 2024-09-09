from user.super_admin.super_admin_func import add_admin, remove_admin, show_admin, edit_admin, show_all_users, \
    show_all_admins, show_all_employees, show_all_couriers, show_all_managers


def admin_management_menu():
    """
    Function to handle admin management menu for super admin.
    """
    print("\nWelcome, Super Admin!\n"
          "Admin Management Menu:\n"
          "1. Add Admin\n"
          "2. Remove Admin\n"
          "3. Show Admin\n"
          "4. Edit Admin\n"
          "5. Back\n")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_admin()

    elif choice == '2':
        remove_admin()

    elif choice == '3':
        show_admin()

    elif choice == '4':
        edit_admin()

    elif choice == '5':
        print("Backing...")
        return None

    else:
        print("Invalid choice. Please try again.")

    return admin_management_menu()


def statistics_menu():
    """
    Function to handle statistics menu for super admin.
    """
    print("\nWelcome, Super Admin!\n"
          "Statistics Menu:\n"
          "1. Show All Users\n"
          "2. Show All Admins\n"
          "3. Show All Employees\n"
          "4. Show All Couriers\n"
          "5. Show All Managers\n"
          "6. Back\n")
    choice = input("Enter your choice: ")

    if choice == '1':
        show_all_users()

    elif choice == '2':
        show_all_admins()

    elif choice == '3':
        show_all_employees()

    elif choice == '4':
        show_all_couriers()

    elif choice == '5':
        show_all_managers()


    elif choice == '6':
        print("Backing...")
        return None

    else:
        print("Invalid choice. Please try again.")

    return statistics_menu()


def super_admin_menu():
    """
    Handles the admin menu for a specific user.
    """
    print("\n1. Admin Management(CRUD)\n"
          "2. Statistics\n"
          "3. Logout\n")
    choice = input("Enter your choice: ")

    if choice == '1':
        admin_management_menu()

    elif choice == '2':
        statistics_menu()

    elif choice == '3':
        print("Logging out...")
        return None

    else:
        print("Invalid choice. Please try again.")

    return super_admin_menu()
