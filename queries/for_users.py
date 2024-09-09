from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


def create_users_table_query() -> None:
    """
    Creates a query for creating a table for storing users.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS users (
        id BIGSERIAL PRIMARY KEY,
        email VARCHAR(64) NOT NULL UNIQUE,
        password VARCHAR(64) NOT NULL,
        first_name VARCHAR(64) NOT NULL,
        last_name VARCHAR(64) NOT NULL,
        role_id INT REFERENCES user_role(id) NOT NULL,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW(),
        status BOOLEAN DEFAULT TRUE
    );
    """)
    return None


def get_user_from_id_query(user_id: int) -> DictRow:
    """
    Creates a query for retrieving a user by their ID from the database.

    Args:
        user_id (int): The ID of the user.

    Returns:
        DictRow: The retrieved user.
    """
    query = "SELECT * FROM users WHERE id = %s AND status = %s;"
    params = (user_id, True)
    result = execute_query(query, params, fetch='one')
    return result


def get_user_from_email_query(email: str) -> DictRow:
    """
    Creates a query for retrieving a user by their email from the database.

    Args:
        email (str): The email address of the user.

    Returns:
        DictRow: The retrieved user.
    """
    query = "SELECT * FROM users WHERE email = %s AND status = %s;"
    params = (email, True)
    result = execute_query(query, params, fetch='one')
    return result


def insert_user_query(email: str, password: str, first_name: str, last_name: str, role_id: int) -> None:
    """
    Creates a query for inserting a new user into the database.

    Args:
        email (str): The email address of the user.
        password (str): The password for the user.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        role_id (int): The ID of the user's role.
    """
    query = """
    INSERT INTO users (email, password, first_name, last_name, role_id)
    VALUES (%s, %s, %s, %s, %s);
    """
    params = (email, password, first_name, last_name, role_id)
    execute_query(query, params)
    return None


def update_user_query(user_id: int, email: str, password: str, first_name: str, last_name: str, role_id: int) -> None:
    """
    Creates a query for updating a user's information in the database.

    Args:
        user_id (int): The ID of the user.
        email (str): The email address of the user.
        password (str): The password for the user.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        role_id (int): The ID of the user's role.
    """
    query = """
    UPDATE users
    SET email = %s, password = %s, first_name = %s, last_name = %s, role_id = %s
    WHERE id = %s AND status = %s;
    """
    params = (email, password, first_name, last_name, role_id, user_id, True)
    execute_query(query, params)
    return None


def delete_user_query(user_id: int) -> None:
    """
    Creates a query for deleting a user from the database.

    Args:
        user_id (int): The ID of the user.
    """
    query = "UPDATE users SET status = %s WHERE id = %s;"
    params = (False, user_id)
    execute_query(query, params)
    return None


def get_all_users_query() -> list:
    """
    Creates a query for retrieving all users from the database.

    Returns:
        List[DictRow]: The retrieved users.
    """
    query = "SELECT * FROM users WHERE status = %s;"
    params = (True,)
    result = execute_query(query, params, fetch='all')
    return result


def get_users_by_role_query(role_id: int) -> list:
    """
    Creates a query for retrieving users by their role ID from the database.

    Args:
        role_id (int): The ID of the user's role.

    Returns:
        List[DictRow]: The retrieved users.
    """
    query = "SELECT * FROM users WHERE role_id = %s AND status = %s;"
    params = (role_id, True)
    result = execute_query(query, params, fetch='all')
    return result
