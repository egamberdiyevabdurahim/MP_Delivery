from queries.for_courier import get_courier_from_user_id_query
from queries.for_employee import get_employee_from_user_id
from queries.for_users import get_user_from_email_query, update_user_query, delete_user_query, get_all_users_query, \
    get_users_by_role_query
from queries.for_user_role import get_user_role_from_name_query

from auth.register import register
from utils.printer import user_printer, employee_printer, courier_printer, manager_printer


# ADMIN MANAGEMENT

def create_admin(email: str = None):
    """
    Creates a new admin user with default role 'admin'.
    """
    if email is None:
        email = input("Enter Admin's Email: ")

    user = get_user_from_email_query(email)
    if not user:
        print("Invalid Email\n"
              "Please try again")

    elif user['role_id'] == get_user_role_from_name_query('admin')['id']:
        print(f"{user['first_name']} {user['last_name']}'s role is already Admin!")
        return None

    else:
        role = get_user_role_from_name_query('admin')
        update_user_query(email=user['email'], password=user['password'], first_name=user['first_name'],
                          last_name=user['last_name'], role_id=role['id'], user_id=user['id'])
        print(f"{user['first_name']} {user['last_name']}'s role Changed to Admin!")
        return None

    return create_admin()


def add_admin():
    """
    Creates a new admin user.
    """
    print("Is Admin Registered to MP Delivery If Not Registered Enter y else Enter n")
    is_created = input("Enter(y/n): ").strip() == 'y'
    if is_created:
        create_admin()

    else:
        email = register()
        create_admin(email)

    return None


def remove_admin_second_func(user):
    """
    Removes an admin user by updating the role to 'user'.
    """
    role = get_user_role_from_name_query('user')
    update_user_query(email=user['email'], password=user['password'], first_name=user['first_name'],
                      last_name=user['last_name'], role_id=role['id'], user_id=user['id'])
    print(f"{user['first_name']} {user['last_name']}'s role Changed to User!")
    return None


def delete_admin(user):
    """
    Deletes an admin user fully.
    """
    delete_user_query(user['id'])
    print(f"{user['first_name']} {user['last_name']}'s Deleted Successfully!")
    return None


def remove_admin():
    """
    Removes an admin user.
    """
    print("Do you want to remove admin or Delete admin fully?")
    choice = input("Enter(remove/delete): ").strip() == 'remove'

    email = input("Enter Admin's Email: ")
    user = get_user_from_email_query(email)

    if not user:
        print("Invalid Email\n"
              "Please try again")
        return None

    elif user['role_id'] != get_user_role_from_name_query('admin')['id']:
        print(f"{user['first_name']} {user['last_name']}'s role is not Admin!")
        return None

    if choice:
        remove_admin_second_func(user)

    else:
        delete_admin(user)

    return None


def show_admin(email: str=None):
    """
    Shows all admin users.
    """
    if email is None:
        email = input("Enter Admin's Email: ")

    user = get_user_from_email_query(email)
    if not user:
        print("Invalid Email\n"
              "Please try again")

    elif user['role_id']!= get_user_role_from_name_query('admin')['id']:
        print(f"{user['first_name']} {user['last_name']}'s role is not Admin!")

    else:
        print(f"\nAdmin: {user['first_name']} {user['last_name']}\n"
              f"Email: {user['email']}\n"
              f"Password: {user['password']}\n"
              f"Registered At: {user['created_at']}\n")

    return None


def edit_admin():
    """
    Edits an admin user's details.
    """
    email = input("Enter Admin's Email: ")
    user = get_user_from_email_query(email)
    if not user:
        print("Invalid Email\n"
              "Please try again")

    elif user['role_id'] != get_user_role_from_name_query('admin')['id']:
        print(f"{user['first_name']} {user['last_name']}'s role is not Admin!")

    else:
        print("Enter the new details:")
        new_password = input("Enter New Password or tap enter to skip: ").strip()
        new_first_name = input("Enter New First Name or tap enter to skip: ").strip()
        new_last_name = input("Enter New Last Name or tap enter to skip: ").strip()

        if not new_password:
            new_password = user['password']

        if not new_first_name:
            new_first_name = user['first_name']

        if not new_last_name:
            new_last_name = user['last_name']

        update_user_query(email=email, password=new_password, first_name=new_first_name, last_name=new_last_name,
                          user_id=user['id'], role_id=user['role_id'])
        print(f"{user['first_name']} {user['last_name']}'s Details Updated Successfully!")
        show_admin(email)

    return None


# STATISTICS

def show_all_users():
    """
    Shows all users.
    """
    users = get_users_by_role_query(get_user_role_from_name_query('user')['id'])
    if not users:
        print("No Users Found!")
        return None

    for user in users:
        user_printer(user)

    return None


def show_all_admins():
    """
    Shows all admins.
    """
    users = get_users_by_role_query(get_user_role_from_name_query('admin')['id'])
    if not users:
        print("No Admins Found!")
        return None

    for user in users:
        user_printer(user)

    return None


def show_all_employees():
    """
    Shows all employees.
    """
    users = get_users_by_role_query(get_user_role_from_name_query('employee')['id'])
    if not users:
        print("No Employees Found!")
        return None

    for user in users:
        employee_data = get_employee_from_user_id(user['id'])
        employee_printer(users+employee_data)

    return None


def show_all_couriers():
    """
    Shows all couriers.
    """
    users = get_users_by_role_query(get_user_role_from_name_query('courier')['id'])
    if not users:
        print("No Couriers Found!")
        return None

    for user in users:
        courier_data = get_courier_from_user_id_query(user['id'])
        courier_printer(users+courier_data)

    return None


def show_all_managers():
    """
    Shows all managers.
    """
    users = get_users_by_role_query(get_user_role_from_name_query('manager')['id'])
    if not users:
        print("No Managers Found!")
        return None

    for user in users:
        manager_printer(user)

    return None
