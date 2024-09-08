def user_menu():
    print("""
1. Place an order
2. My orders history
3. My active order
4. Update profile
5. Logout
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
    elif user_input == '5':
        pass
    else:
        print("Invalid choice. Please try again")
        return user_menu()