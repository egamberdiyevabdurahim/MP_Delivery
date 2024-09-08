def courier_menu():
    print("""
1. Deliver order 
2. My deliver history
3. My actie deliver
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
        return courier_menu()