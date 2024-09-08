from queries.for_users import insert_user_query, get_user_from_email_query, get_user_from_id_query
from queries.for_user_role import get_all_user_roles_query, get_user_role_from_id_query
from queries.for_regions import get_all_regions_query, get_region_from_id_query
from queries.for_courier import insert_courier_query, get_courier_from_phone_number_query
from queries.for_purse import insert_purse_query, get_purse_from_id_query
from queries.for_employee import insert_employee_query

from utils import additions


# def create_courier(user_id: int):
#     """
#     Inserts a new courier into the database.
#     """
#     phone_number: str = input("Enter your phone number: ")
#     # Check if the phone number is unique
#     while not phone_number.startswith(additions.phone_number_details):
#         print("Invalid phone number format. Please use the following format: +7 (XXX) XXX-XX-XX")
#         phone_number = input("Re-Enter your phone number: ")
#
#     region_id: int = int(input("Enter your region ID: "))
#     # Check if the region exists
#     while not get_region_from_id_query(region_id):
#         print("Invalid region ID!")
#         region_id = int(input("Re-Enter your region ID: "))
#
#     purse_id: int = int(input("Enter your purse ID: "))
#     # Check if the purse exists
#     while not get_purse_from_id_


def register():
    """
    Handles the registration process for a new user.
    """
    email: str = input("Enter your email: ")
    # Check if the email address is unique
    while not email.startswith(additions.email_details):
        print("Invalid email format. Please use one of the following formats: @mail.ru, @gmail.com, @icloud.com")
        email = input("Re-Enter your email: ")

    password: str = input("Enter your password: ")
    while not password or len(password) < 8:
        print("Password must be at least 8 characters long!")
        password = input("Re-Enter your password: ")

    password_confirmation: str = input("Confirm your password: ")
    # Check if the password and password confirmation match
    while password!= password_confirmation:
        print("Passwords do not match!")
        password_confirmation = input("Re-Confirm your password: ")

    first_name: str = input("Enter your First Name: ")
    while not first_name:
        print("First Name is required!")
        first_name = input("Re-Enter your First Name: ")

    last_name: str = input("Enter your Last Name: ")
    while not last_name:
        print("Last Name is required!")
        last_name = input("Re-Enter your Last Name: ")

    roles_data = get_all_user_roles_query()
    for role_name in roles_data:
        print(f"{role_name['id']}. {role_name['name']}")

    role_id: str = input("Enter your role ID: ")

    # Check if the role ID exists in the database
    while not role_id in [role_data['id'] for role_data in roles_data]:
        print("Invalid class ID. Please try again or Enter stop for Exit.")
        role_id = input("Re-Enter your role ID: ")

        if role_id.lower() == "stop":
            return None

    role_data = get_user_role_from_id_query(int(role_id))

    # Create a new user in the database
    insert_user_query(email=email, password=password, role_id=int(role_id), first_name=first_name, last_name=last_name)

    if role_data['name'] == "courier":
        pass

    elif role_data['name'] == "employee":
        pass

    print("Congratulations!!!")
    print(f"{first_name} {last_name} You Registered Successfully to MP Delivery!")
    return email