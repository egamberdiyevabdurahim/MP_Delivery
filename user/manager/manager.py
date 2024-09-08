def manager_menu():
    print("""
1. Product management(CRUD)
2. Branch management(CRUD)
3. Employee management(CRUD)
4. Logout
""")
    user_input = input("Enter your choice: ")
    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == '4':
        pass
    else:
        print("Invalid choice. Please try again")
        return manager_menu()