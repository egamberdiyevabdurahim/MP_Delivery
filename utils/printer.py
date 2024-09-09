from queries.for_branch import get_branch_from_id_query
from queries.for_company import get_company_from_manager_id_query
from queries.for_purse import get_purse_from_id_query
from queries.for_regions import get_region_from_id_query


def user_printer(user):
    print(f"\nUser: {user['first_name']} {user['last_name']}\n"
          f"Email: {user['email']}\n"
          f"Password: {user['password']}\n"
          f"Registered At: {user['created_at']}\n")
    return None


def manager_printer(manager_data):
    print(f"\nManager: {manager_data['first_name']} {manager_data['last_name']}\n"
          f"Email: {manager_data['email']}\n"
          f"Password: {manager_data['password']}\n"
          f"Registered At: {manager_data['created_at']}\n"
          f"Company: {get_company_from_manager_id_query(manager_data['id'])}\n")
    return None


def employee_printer(employee_data):
    print(f"\nEmployee: {employee_data['first_name']} {employee_data['last_name']}\n"
          f"Email: {employee_data['email']}\n"
          f"Password: {employee_data['password']}\n"
          f"Registered At: {employee_data['created_at']}\n"
          f"Phone: {employee_data['phone_number']}\n"
          f"Region: {get_region_from_id_query(employee_data['region_id'])}\n"
          f"Branch: {get_branch_from_id_query(employee_data['branch_id'])['name']}\n")
    return None


def courier_printer(courier_data):
    print(f"\nCourier: {courier_data['first_name']} {courier_data['last_name']}\n"
          f"Email: {courier_data['email']}\n"
          f"Password: {courier_data['password']}\n"
          f"Registered At: {courier_data['created_at']}\n"
          f"Phone: {courier_data['phone_number']}\n"
          f"Region: {get_region_from_id_query(courier_data['region_id'])}\n"
          f"Price for Delivering: {courier_data['price_for_delivering']}\n"
          f"Purse: {get_purse_from_id_query(courier_data['purse_id'])['amount']}\n")
    return None
