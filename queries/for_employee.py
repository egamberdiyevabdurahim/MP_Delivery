from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


def create_employee_table_query() -> None:
    """
    Creates a table for storing employee.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS employee (
        id BIGSERIAL PRIMARY KEY,
        branch_id BIGINT REFERENCES branch(id),
        user_id BIGINT REFERENCES users(id) NOT NULL,
        region_id BIGINT REFERENCES regions(id) NOT NULL,
        phone_number VARCHAR(64) NOT NULL UNIQUE,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW(),
        status BOOLEAN DEFAULT TRUE
    );
    """)
    return None


def get_employee_from_id_query(employee_id: int) -> DictRow:
    """
    Retrieves an employee from the database by its ID.

    Args:
        employee_id (int): The ID of the employee to retrieve.

    Returns:
        DictRow: The retrieved employee.
    """
    query = "SELECT * FROM employee WHERE id = %s AND status = %s;"
    params = (employee_id, True)
    result = execute_query(query, params, fetch='one')
    return result


def get_employee_from_phone_number_query(phone_number: str) -> DictRow:
    """
    Retrieves an employee from the database by their phone number.

    Args:
        phone_number (str): The phone number of the employee to retrieve.

    Returns:
        DictRow: The retrieved employee.
    """
    query = "SELECT * FROM employee WHERE phone_number = %s AND status = %s;"
    params = (phone_number, True)
    result = execute_query(query, params, fetch='one')
    return result


def get_employee_from_user_id(user_id: int):
    """
    Retrieves employees associated with a user from the database.

    Args:
        user_id (int): The ID of the user.

    Returns:
        list: The retrieved employees.
    """
    query = "SELECT * FROM employee WHERE user_id = %s AND status = %s;"
    params = (user_id, True)
    result = execute_query(query, params, fetch='all')
    return result


def get_employees_from_branch_id_query(branch_id: int) -> list:
    """
    Retrieves employees associated with a branch from the database.

    Args:
        branch_id (int): The ID of the branch.

    Returns:
        list: The retrieved employees.
    """
    query = "SELECT * FROM employee WHERE branch_id = %s AND status = %s;"
    params = (branch_id, True)
    result = execute_query(query, params, fetch='all')
    return result


def get_unemployed_employees_query() -> list:
    """
    Retrieves unemployed employees from the database.

    Returns:
        list: The retrieved unemployed employees.
    """
    query = "SELECT * FROM employee WHERE branch_id IS NULL AND status = %s;"
    params = (True,)
    result = execute_query(query, params, fetch='all')
    return result


def insert_employee_query(user_id: int, region_id: int, phone_number: str, branch_id: int=None) -> None:
    """
    Inserts a new employee into the database.

    Args:
        user_id (int): The ID of the user associated with the employee.
        region_id (int): The ID of the region the employee works in.
        phone_number (str): The phone number of the employee.
        branch_id (int, optional): The ID of the branch the employee works in. Defaults to None.

    Returns:
        None.
    """
    query = "INSERT INTO employee (user_id, region_id, phone_number, branch_id) VALUES (%s, %s, %s, %s);"
    params = (user_id, region_id, phone_number, branch_id)
    execute_query(query, params)
    return None


def update_employee_query(employee_id: int, region_id: int, phone_number: str, branch_id: int=None) -> None:
    """
    Updates an employee's information in the database.

    Args:
        employee_id (int): The ID of the employee.
        region_id (int): The new ID of the region the employee works in.
        phone_number (str): The new phone number of the employee.
        branch_id (int, optional): The new ID of the branch the employee works in. Defaults to None.

    Returns:
        None.
    """
    query = "UPDATE employee SET phone_number = %s, region_id = %s, branch_id = %s WHERE id = %s;"
    params = (phone_number, region_id, branch_id, employee_id)
    execute_query(query, params)
    return None


def delete_employee_query(employee_id) -> None:
    """
    Deletes an employee from the database.

    Args:
        employee_id (int): The ID of the employee to delete.

    Returns:
        None.
    """
    query = "UPDATE employee SET status = %s WHERE id = %s;"
    params = (False, employee_id)
    execute_query(query, params)
    return None


def get_all_employees_query() -> None:
    """
    Creates a query for retrieving all employees from the database.

    Returns:
    List[DictRow].
    """
    query = "SELECT * FROM employee WHERE status = %s;"
    params = (True,)
    result = execute_query(query, params, fetch='all')
    return result


def search_employee(employee_id: int):
    """
    Search for employee in the employee table.
    """
    query = "SELECT * FROM employee WHERE id LIKE %s;"
    result = execute_query(query, params=("%" + employee_id + "%",), fetch="all")
    if result:
        print("employee:")
        for employee in result:
            print(f"""ID: {employee[0]}, User ID: {employee[1]}, Banch ID: {employee[2]}, 
                    Phone_number: {employee[3]}, Region ID: {employee[4]}""")
    else:
        print("No employee found.")
    return None