from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


def create_user_role_table_query() -> None:
    """
    Creates a table for storing user roles.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS user_role (
        id BIGSERIAL PRIMARY KEY,
        name VARCHAR(64) NOT NULL UNIQUE
    );
    """)
    return None


def get_user_role_from_id_query(role_id: int) -> DictRow:
    """
    Retrieves a role from the database by its ID.

    Args:
        role_id (int): The ID of the role to retrieve.

    Returns:
        DictRow: The retrieved role.
    """
    query = f"SELECT * FROM user_role WHERE id = %s;"
    params = (role_id,)
    result = execute_query(query, params, fetch='one')
    return result


def get_user_role_from_name_query(name: str) -> DictRow:
    """
    Retrieves a role from the database by its name.

    Args:
        name (str): The name of the role to retrieve.

    Returns:
        DictRow: The retrieved role.
    """
    query = f"SELECT * FROM user_role WHERE name = %s;"
    params = (name,)
    result = execute_query(query, params, fetch='one')
    return result


def insert_user_role_query(name: str) -> None:
    """
    Inserts a new role into the database.

    Args:
        name (str): The name of the new role.

    Returns:
        None.
    """
    query = "INSERT INTO user_role (name) VALUES (%s);"
    params = (name,)
    execute_query(query, params)
    return None


def update_user_role_query(role_id: int, name: str) -> None:
    """
    Updates a role's name in the database.

    Args:
        role_id (int): The ID of the role to update.
        name (str): The new name of the role.

    Returns:
        None.
    """
    query = "UPDATE user_role SET name = %s WHERE id = %s;"
    params = (name, role_id)
    execute_query(query, params)
    return None


def delete_user_role_query(role_id: int) -> None:
    """
    Deletes a role from the database.

    Args:
        role_id (int): The ID of the role to delete.

    Returns:
        None.
    """
    query = "DELETE FROM user_role WHERE id = %s"
    params = (role_id,)
    execute_query(query, params)
    return None


def get_all_user_roles_query() -> list:
    """
    Retrieves all roles from the database.

    Returns:
        List[DictRow]: The retrieved roles.
    """
    query = "SELECT * FROM user_role;"
    result = execute_query(query, fetch='all')
    return result
