from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


def create_category_table_query() -> None:
    """
    Creates a table for storing categories.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS category (
        id BIGSERIAL PRIMARY KEY,
        name VARCHAR(64) UNIQUE NOT NULL,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW(),
        status BOOLEAN DEFAULT TRUE
    );
    """)
    return None


def get_category_from_id_query(category_id: int) -> DictRow:
    """
    Retrieves a category from the database by its ID.

    Args:
        category_id (int): The ID of the category to retrieve.

    Returns:
        DictRow: The retrieved category.
    """
    query = "SELECT * FROM category WHERE id = %s AND status = %s;"
    params = (category_id, True)
    result = execute_query(query, params, fetch='one')
    return result


def get_category_from_name_query(name: str) -> DictRow:
    """
    Retrieves a category from the database by its name.

    Args:
        name (str): The name of the category to retrieve.

    Returns:
        DictRow: The retrieved category.
    """
    query = "SELECT * FROM category WHERE name = %s AND status = %s;"
    params = (name, True)
    result = execute_query(query, params, fetch='one')
    return result


def insert_category_query(name: str) -> None:
    """
    Inserts a new category into the database.

    Args:
        name (str): The name of the new category.
    """
    query = "INSERT INTO category (name) VALUES (%s);"
    params = (name,)
    execute_query(query, params)
    return None


def update_category_query(category_id: int, name: str) -> None:
    """
    Updates an existing category in the database.

    Args:
        category_id (int): The ID of the category to update.
        name (str): The new name for the category.
    """
    query = "UPDATE category SET name = %s, updated_at = NOW() WHERE id = %s;"
    params = (name, category_id)
    execute_query(query, params)
    return None


def delete_category_query(category_id: int) -> None:
    """
    Deletes a category from the database.

    Args:
        category_id (int): The ID of the category to delete.
    """
    query = "UPDATE category SET status = %s WHERE id = %s;"
    params = (False, category_id)
    execute_query(query, params)
    return None


def get_all_categories_query() -> list:
    """
    Retrieves all categories from the database.

    Returns:
        list: The retrieved categories.
    """
    query = "SELECT * FROM category WHERE status = %s;"
    params = (True,)
    result = execute_query(query, params, fetch='all')
    return result
