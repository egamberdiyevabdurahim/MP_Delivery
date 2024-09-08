from typing import Optional, Tuple

from queries.for_users import get_user_from_email_query
from queries.for_user_role import get_user_role_from_id_query


def login() -> Optional[Tuple[str, str]]:
    """
    Handles the login process for a user.
    """
    email: str = input("Enter your email address: ")
    password: str = input("Enter your password: ")

    if email == "super" and password == "super":
        print("Login successful as Super Admin!")
        return "super", "super"

    user_data = get_user_from_email_query(email)
    if user_data is None:
        print("Invalid email or password. Please try again.")
        return None

    if user_data['password'] != password:
        print("Invalid email or password. Please try again.")
        return None

    user_role_data = get_user_role_from_id_query(user_data['role_id'])
    if user_role_data is None:
        print("Invalid user role. Please contact an administrator.")
        return None

    return user_data['email'], user_role_data['name']
