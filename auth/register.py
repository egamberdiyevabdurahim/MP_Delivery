from queries.for_users import insert_user_query, get_user_from_email_query, get_user_from_id_query
from queries.for_user_role import get_all_user_roles_query, get_user_role_from_id_query, get_user_role_from_name_query
from queries.for_regions import get_all_regions_query, get_region_from_id_query
from queries.for_courier import insert_courier_query, get_courier_from_phone_number_query
from queries.for_purse import insert_purse_query, get_purse_from_id_query
from queries.for_employee import insert_employee_query

from utils import additions


def register():
    """
    Handles the registration process for a new user.
    """
    email: str = input("Enter your email: ")
    # Check if the email address is unique
    while not email.endswith(additions.email_details):
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

    role_data = get_user_role_from_name_query("user")

    # Create a new user in the database
    insert_user_query(email=email, password=password, role_id=role_data['id'], first_name=first_name, last_name=last_name)
    print("Congratulations!!!")
    print(f"{first_name} {last_name} You Registered Successfully to MP Delivery!")
    return email
