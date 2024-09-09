# from auth.register import register
# from queries.for_user_role import get_user_role_from_name_query
# from queries.for_users import get_user_from_email_query, update_user_query
#
#
# # MANAGER MANAGEMENT
#
#
# # def add_manager_to_company_second_func(user):
# #     """
# #     Adds a manager user to a company by updating the user's role to 'manager' and adding them to the company.
# #     """
# #     companies_data =
#
#
# def add_manager_to_company(email: str = None):
#     """
#     Creates a new manager user and adds them to a company.
#     """
#     email = register() if email is None else email
#     user = get_user_from_email_query(email)
#
#     if not user:
#         print("Invalid Email\n"
#               "Please try again")
#         return None
#
#     elif user['role_id'] != get_user_role_from_name_query('manager')['id']:
#         print(f"{user['first_name']} {user['last_name']}'s role is not Manager!")
#         return None
#
#     else:
#         role = get_user_role_from_name_query('manager')
#
#
# def create_manager(email: str = None):
#     """
#     Creates a new manager user with default role 'manager'.
#     """
#     if email is None:
#         email = input("Enter Manager's Email: ")
#
#     user = get_user_from_email_query(email)
#     if not user:
#         print("Invalid Email\n"
#               "Please try again")
#
#     elif user['role_id'] == get_user_role_from_name_query('manager')['id']:
#         print(f"{user['first_name']} {user['last_name']}'s role is already Manager!")
#         return None
#
#     else:
#         role = get_user_role_from_name_query('manager')
#         update_user_query(email=user['email'], password=user['password'], first_name=user['first_name'],
#                           last_name=user['last_name'], role_id=role['id'], user_id=user['id'])
#         print(f"{user['first_name']} {user['last_name']}'s role Changed to Manager!")
#         return None
#
#     return create_manager()
#
#
# def add_manager():
#     """
#     Creates a new manager user.
#     """
#     print("Is Manager Registered to MP Delivery If Not Registered Enter y else Enter n")
#     is_created = input("Enter(y/n): ").strip() == 'y'
#     if is_created:
#         create_manager()
#
#     else:
#         email = register()
#         create_manager(email)
#
#     return None
#
#
# def remove_manager_second_func(user):
#     """
#     Removes an admin user by updating the role to 'user'.
#     """
#     role = get_user_role_from_name_query('user')
#     update_user_query(email=user['email'], password=user['password'], first_name=user['first_name'],
#                       last_name=user['last_name'], role_id=role['id'], user_id=user['id'])
#     print(f"{user['first_name']} {user['last_name']}'s role Changed to User!")
#     return None
#
#
# def delete_admin(user):
#     """
#     Deletes an admin user fully.
#     """
#     delete_user_query(user['id'])
#     print(f"{user['first_name']} {user['last_name']}'s Deleted Successfully!")
#     return None
#
#
# def remove_admin():
#     """
#     Removes an admin user.
#     """
#     print("Do you want to remove admin or Delete admin fully?")
#     choice = input("Enter(remove/delete): ").strip() == 'remove'
#
#     email = input("Enter Admin's Email: ")
#     user = get_user_from_email_query(email)
#
#     if not user:
#         print("Invalid Email\n"
#               "Please try again")
#         return None
#
#     elif user['role_id'] != get_user_role_from_name_query('admin')['id']:
#         print(f"{user['first_name']} {user['last_name']}'s role is not Admin!")
#         return None
#
#     if choice:
#         remove_admin_second_func(user)
#
#     else:
#         delete_admin(user)
#
#     return None
#
#
# def show_admin(email: str=None):
#     """
#     Shows all admin users.
#     """
#     if email is None:
#         email = input("Enter Admin's Email: ")
#
#     user = get_user_from_email_query(email)
#     if not user:
#         print("Invalid Email\n"
#               "Please try again")
#
#     elif user['role_id']!= get_user_role_from_name_query('admin')['id']:
#         print(f"{user['first_name']} {user['last_name']}'s role is not Admin!")
#
#     else:
#         print(f"\nAdmin: {user['first_name']} {user['last_name']}\n"
#               f"Email: {user['email']}\n"
#               f"Password: {user['password']}\n"
#               f"Registered At: {user['created_at']}\n")
#
#     return None
#
#
# def edit_admin():
#     """
#     Edits an admin user's details.
#     """
#     email = input("Enter Admin's Email: ")
#     user = get_user_from_email_query(email)
#     if not user:
#         print("Invalid Email\n"
#               "Please try again")
#
#     elif user['role_id'] != get_user_role_from_name_query('admin')['id']:
#         print(f"{user['first_name']} {user['last_name']}'s role is not Admin!")
#
#     else:
#         print("Enter the new details:")
#         new_password = input("Enter New Password or tap enter to skip: ").strip()
#         new_first_name = input("Enter New First Name or tap enter to skip: ").strip()
#         new_last_name = input("Enter New Last Name or tap enter to skip: ").strip()
#
#         if not new_password:
#             new_password = user['password']
#
#         if not new_first_name:
#             new_first_name = user['first_name']
#
#         if not new_last_name:
#             new_last_name = user['last_name']
#
#         update_user_query(email=email, password=new_password, first_name=new_first_name, last_name=new_last_name,
#                           user_id=user['id'], role_id=user['role_id'])
#         print(f"{user['first_name']} {user['last_name']}'s Details Updated Successfully!")
#         show_admin(email)
#
#     return None
