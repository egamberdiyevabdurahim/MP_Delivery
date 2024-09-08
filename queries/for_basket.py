from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


def create_basket_table_query() -> None:
    """
    Creates a table for storing baskets.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS basket (
        id BIGSERIAL PRIMARY KEY,
        user_id BIGINT REFERENCES users(id) NOT NULL,
        is_active BOOLEAN DEFAULT TRUE,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW(),
        status BOOLEAN DEFAULT TRUE
    );
    """)
    return None


def get_basket_from_id_query(basket_id: int) -> DictRow:
    """
    Retrieves a basket from the database by its ID.

    Args:
        basket_id (int): The ID of the basket to retrieve.

    Returns:
        DictRow: The retrieved basket.
    """
    query = "SELECT * FROM basket WHERE id = %s AND status = %s;"
    params = (basket_id, True)
    result = execute_query(query, params, fetch='one')
    return result


def get_basket_from_user_id_query(user_id: int) -> DictRow:
    """
    Retrieves a basket from the database by the user's ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        DictRow: The retrieved basket.
    """
    query = "SELECT * FROM basket WHERE user_id = %s AND is_active = %s;"
    params = (user_id, True)
    result = execute_query(query, params, fetch='one')
    return result


def insert_basket_query(user_id: int) -> None:
    """
    Inserts a new basket into the database.

    Args:
        user_id (int): The ID of the user who will own the basket.
    """
    query = "INSERT INTO basket (user_id) VALUES (%s);"
    params = (user_id,)
    execute_query(query, params)
    return None


def disable_basket_query(basket_id: int) -> None:
    """
    Disables a basket for a user.

    Args:
        basket_id (int): The ID of the basket to disable.
    """
    query = "UPDATE basket SET is_active = %s WHERE id = %s;"
    params = (False, basket_id)
    execute_query(query, params)
    return None


def delete_basket_query(basket_id: int) -> None:
    """
    Deletes a basket from the database.

    Args:
        basket_id (int): The ID of the basket to delete.
    """
    query = "UPDATE basket SET status = %s WHERE id = %s;"
    params = (False, basket_id)
    execute_query(query, params)
    return None


def get_all_baskets_query() -> list:
    """
    Retrieves all active baskets from the database.

    Returns:
        list: The retrieved baskets.
    """
    query = "SELECT * FROM basket WHERE status = %s;"
    params = (True,)
    result = execute_query(query, params, fetch='all')
    return result
